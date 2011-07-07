from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase

from homebrewit.contest.management.commands.judgecontest import JudgeContestCommand
from homebrewit.contest.models import *
from homebrewit.contest.views import *


class ContestViewsTest(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'users', 'userprofiles', 'judgingresults']

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

		response = self.client.post('/contest/register', {'beer_name': "Patrick's super skunky IPA", 'style': '1'})
		entry = Entry.objects.get(beer_name="Patrick's super skunky IPA")
		self.assert_(entry.user.username == 'patrick')

	def test_register__post_already_entered(self):
		response = self.client.post('/contest/register', {'beer_name': "Patrick's super skunky IPA", 'style': '1'})
		self.assertRaises(Entry.DoesNotExist, Entry.objects.get, beer_name="Patrick's super skunky IPA")


	def test_contest_year(self):
		response = self.client.get('/contest/2011/')
		self.assertTemplateUsed(response, 'homebrewit_contest_year.html')
		self.assert_(response.context['year'] == 2011)
		self.assert_(len(response.context['styles']) == 8)

		ipa = BeerStyle.objects.get(name='IPA')
		self.assert_(len(response.context['styles'][ipa]['entries']) == 4)
		self.assert_(not response.context['styles'][ipa]['has_more'])


	def test_entry(self):
		response = self.client.get('/contest/2011/styles/1/entries/1')
		self.assertTemplateUsed(response, 'homebrewit_contest_entry.html')
		self.assert_(response.context['entry'].beer_name == 'Beer name')
		self.assert_(len(response.context['judging_results']) == 1)


	def test_style(self):
		response = self.client.get('/contest/2011/styles/1')
		self.assertTemplateUsed(response, 'homebrewit_contest_style.html')
		self.assert_(response.context['style'].name == 'IPA')
		self.assert_(len(response.context['entries']) == 4)
		self.assert_(response.context['address'])

	
	def test_winner_styles(self):
		response = self.client.get('/contest/winner-styles.css')
#		self.assert_('Cache-Control' in str(response))
#		self.assert_('ETag' in str(response))

		content = response.content
		self.assert_('a[href*="user/patrickomatic"]:after' in content)
		self.assert_('a[href*="user/musashiXXX"]:after' in content)
		self.assert_(not 'a[href*="user/loser"]:after' in content)


class ContestModelsTest(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'judgingresults', 'userprofiles', 'users' ]

	def setUp(self):
		self.ipa_style = BeerStyle.objects.get(name='IPA')
		self.ipa_style = BeerStyle.objects.get(name='IPA')


	def test_get_top_n(self):
		top_2 = Entry.objects.get_top_n(self.ipa_style, 2)
		self.assert_(2 == len(top_2))
		self.assert_('patrick' 			== top_2[0].user.username)
		self.assert_('patrickomatic' 	== top_2[1].user.username)

	def test_get_top_2(self):
		self.assert_(2 == len(Entry.objects.get_top_2(self.ipa_style)))

	def test_get_top_3(self):
		self.assert_(3 == len(Entry.objects.get_top_3(self.ipa_style)))


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
