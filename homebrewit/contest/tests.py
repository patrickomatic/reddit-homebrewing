from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase

from homebrewit.contest.management.commands.judgecontest import JudgeContestCommand
from homebrewit.contest.models import *
from homebrewit.contest.views import *


class ContestViewsTest(TestCase):
	fixtures = ['beerstyles', 'beerstylesubcategories', 'contestyears', 'entries', 'users', 'userprofiles', 'judgingresults']

	def setUp(self):
		self.client.login(username='patrick', password='password')
		self.user = User.objects.get(username='patrick')


	def test_register(self):
		response = self.client.get('/contest/register')
		self.assert_(response.context['form'])

	def test_register__profile_not_set(self):
		self.user.get_profile().delete()
		response = self.client.get('/contest/register')
		self.assertRedirects(response, '/profile/edit?next=/contest/register')

	def test_register__post(self):
		Entry.objects.filter(user=self.user).delete()

		response = self.client.post('/contest/register', {'beer_name': "Patrick's super skunky IPA", 'style': '1', 'special_ingredients': 'poop'})

		self.assert_(response.context['form'].is_valid())

		# the entry now exists
		entry = Entry.objects.get(beer_name="Patrick's super skunky IPA")
		self.assert_(entry is not None)
		self.assert_(entry.user.username == 'patrick')
		self.assert_(entry.special_ingredients == 'poop')
		self.assert_(entry.style_subcategory is None)
		self.assert_(entry.style.id == 1)

		# should send the registration email
		self.assert_(len(mail.outbox) == 1)

	def test_register__post_already_entered(self):
		response = self.client.post('/contest/register', {'beer_name': "Patrick's super skunky IPA", 'style': '1'})
		self.assert_(not response.context['form'].is_valid())
		self.assertRaises(Entry.DoesNotExist, Entry.objects.get, beer_name="Patrick's super skunky IPA")

	def test_register__not_allowing_entries(self):
		Entry.objects.filter(user=self.user).delete()

		contest_year = ContestYear.objects.get_current_contest_year()
		contest_year.allowing_entries = False
		contest_year.save()

		response = self.client.post('/contest/register', {'beer_name': "Patrick's super skunky IPA", 'style': '1'})
		self.assert_(response.status_code == 404)

	def test_register__style_subcategory(self):
		Entry.objects.filter(user=self.user).delete()

		name = 'Super dank Stout'
		response = self.client.post('/contest/register', {'beer_name': name, 'style': 6, 'style_subcategory': 2})

		self.assert_(Entry.objects.get(beer_name=name).style_subcategory.id == 2)

	def test_register__style_subcategory_required(self):
		Entry.objects.filter(user=self.user).delete()

		response = self.client.post('/contest/register', {'beer_name': 'Super dank Stout', 'style': 6})
		
		self.assert_(not response.context['form'].is_valid())


	def test_contest_year(self):
		response = self.client.get('/contest/2011/')
		self.assertTemplateUsed(response, 'homebrewit_contest_year.html')
		self.assert_(response.context['year'] == 2011)
		self.assert_(len(response.context['styles']) == 8)

		stout = BeerStyle.objects.get(name='Stout')
		self.assert_(len(response.context['styles'][stout]['entries']) == 4)
		self.assert_(not response.context['styles'][stout]['has_more'])


	def test_entry(self):
		response = self.client.get('/contest/2011/styles/1/entries/1')

		self.assertTemplateUsed(response, 'homebrewit_contest_entry.html')
		self.assert_(response.context['entry'].beer_name == 'Beer name')
		self.assert_(len(response.context['judging_results']) == 1)


	def test_style(self):
		winner = Entry.objects.filter(style__name='IPA')[0]
		winner.winner = True
		winner.score = 50
		winner.save()

		response = self.client.get('/contest/2011/styles/1')

		self.assertTemplateUsed(response, 'homebrewit_contest_style.html')
		self.assert_(response.context['style'].name == 'IPA')
		self.assert_(len(response.context['entries']) == 4)
		self.assert_(response.context['entries'][0].winner)
		self.assert_(response.context['address'])

	
	def test_winner_styles(self):
		response = self.client.get('/contest/winner-styles.css')

		content = response.content
		self.assert_('a[href*="user/patrickomatic"]:after' in content)
		self.assert_('a[href*="user/musashiXXX"]:after' in content)
		self.assert_(not 'a[href*="user/loser"]:after' in content)


class EntryModelTest(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'judgingresults', 'userprofiles', 'users' ]

	def setUp(self):
		self.stout_style = BeerStyle.objects.get(name='Stout')


	def test_get_top_n(self):
		top_2 = Entry.objects.get_top_n(self.stout_style, 2)
		self.assert_(2 == len(top_2))
		self.assert_('patrick' 			== top_2[0].user.username)
		self.assert_('patrickomatic' 	== top_2[1].user.username)

	def test_get_top_2(self):
		self.assert_(2 == len(Entry.objects.get_top_2(self.stout_style)))

	def test_get_top_3(self):
		self.assert_(3 == len(Entry.objects.get_top_3(self.stout_style)))


	def test_get_all_winners(self):
		winners = Entry.objects.get_all_winners()
		self.assert_(User.objects.get(username='patrick') in winners)
		self.assert_(User.objects.get(username='patrickomatic') in winners)
		self.assert_(User.objects.get(username='musashiXXX') in winners)


	def test_send_shipping_email(self):
		entry = Entry.objects.get(pk=2)
		entry.send_shipping_email()

		entry = Entry.objects.get(pk=2)
		self.assert_(entry.mailed_entry)

		self.assert_(len(mail.outbox) == 1)
		self.assert_('2011 Reddit Homebrew' in mail.outbox[0].subject)
		message = str(mail.outbox[0].message()).replace("\n", " ")
		self.assert_('128 Hilltop Rd' in message)
		self.assert_(not 'None' in message)


	def test_rating_description_str(self):
		self.assert_(JudgingResult.rating_description_str(60).startswith("Outstanding"))
		self.assert_(JudgingResult.rating_description_str(30).startswith("Good"))
		self.assert_(JudgingResult.rating_description_str(1).startswith("Problematic"))

	def test_get_description(self):
		result = BJCPJudgingResult(aroma_score=12, appearance_score=3, flavor_score=20, mouthfeel_score=5, overall_impression_score=10)

		self.assert_(result.get_description().startswith("Outstanding"))

		result = BJCPJudgingResult(aroma_score=1, appearance_score=1, flavor_score=1, mouthfeel_score=1, overall_impression_score=1)
		self.assert_(result.get_description().startswith("Problematic"))

		result = BJCPJudgingResult(aroma_score=20, appearance_score=1, flavor_score=1, mouthfeel_score=1, overall_impression_score=1)
		self.assert_(result.get_description().startswith("Good"))


class ContestYearModelTests(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'judgingresults', 'userprofiles', 'users' ]


	def test_get_current_contest_year(self):
		for y in range(2005, 2011):
			ContestYear(contest_year=y).save()

		self.assert_(ContestYear.objects.get_current_contest_year().contest_year == 2011)


class BeerStyleModelTests(TestCase):
	fixtures = ['beerstyles', 'beerstylesubcategories', 'contestyears', 'entries', 'judgingresults', 'userprofiles', 'users' ]

	def setUp(self):
		self.stout_style = BeerStyle.objects.get(name='Stout')
		self.ipa_style = BeerStyle.objects.get(name='IPA')


	def test_get_subcategories(self):
		self.assert_(len(self.stout_style.get_subcategories()) == 3)

	def test_get_subcategories__none(self):
		self.assert_(len(self.ipa_style.get_subcategories()) == 0)


	def test_has_subcategories(self):
		self.assert_(self.stout_style.has_subcategories())

	def test_has_subcategories__doesnt(self):
		self.assert_(not self.ipa_style.has_subcategories())


class JudgeContestCommandTest(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'users', 'judgingresults']

	def setUp(self):
		self.command = JudgeContestCommand()


	def test_handle(self):
		self.assert_(Entry.objects.filter(winner=True).count() == 3)
		self.command.handle(2011)
		self.assert_(Entry.objects.filter(winner=True).count() == 6)

		# the ipa should now be judged as first place
		ipa = Entry.objects.get(pk=1)
		self.assert_(ipa.winner)
		self.assert_(ipa.rank == 1)
		self.assert_(ipa.score == 63)
