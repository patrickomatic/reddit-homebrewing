from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from homebrewit.contest.management.commands.judgecontest import Command
from homebrewit.contest.models import *
from homebrewit.contest.views import *
from homebrewit.contest.forms import *


class ContestViewsTests(TestCase):
	fixtures = ['beerstyles', 'beerstylesubcategories', 'contestyears', 'entries', 'users', 'userprofiles', 'bjcpjudgingresults', 'judgingresults']

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
		self.assert_('"name": "English Stout"' in response.context['style_data_as_json'])

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

	def test_entry__bjcp_judging_result(self):
		response = self.client.get('/contest/2011/styles/1/entries/2')

		self.assertTemplateUsed(response, 'homebrewit_contest_bjcp_entry.html')
		self.assert_(response.context['entry'].beer_name == 'Beer name')
		self.assert_(response.context['entry'].bjcp_judging_result is not None)
		self.assert_(response.context['form'] is not None)


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


class EntryModelTests(TestCase):
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


class CommandTests(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'users', 'judgingresults', 'bjcpjudgingresults']

	def setUp(self):
		self.command = Command()


	def test_handle(self):
		self.assert_(Entry.objects.filter(winner=True).count() == 3)
		self.command.handle(2011)
		self.assert_(Entry.objects.filter(winner=True).count() == 6)

		# the ipa should now be judged as first place
		ipa = Entry.objects.get(pk=1)
		self.assert_(ipa.winner)
		self.assert_(ipa.rank == 1)
		self.assert_(ipa.score == 63)


class EntryJudgingFormTests(TestCase):
    fixtures = ['judgingform.json']

    def test_access_judges_only(self):
        """
            Only judges have access to the judging form.
        """
        judge_successful_login = self.client.login(username = 'patrickomatic', password = 'patrickomatic')
        self.assertEqual(judge_successful_login, True)
        response = self.client.get('/contest/judgeentry')
        self.assertEqual(response.status_code, 200)

        non_judge_successful_login = self.client.login(username = 'admin', password = 'admin')
        self.assertEqual(non_judge_successful_login, True)
        self.assertRaises(RuntimeError, self.client.get, '/contest/judgeentry')

    def test_entry_selection_filter(self):
        """
            The only entries that should appear in the entry selection dropdown box
            are the entries that pertain to the style category for the currently
            logged-in judge.
        """
        judge_successful_login = self.client.login(username = 'patrickomatic', password = 'patrickomatic')
        response = self.client.get('/contest/judgeentry')
        user = User.objects.get(username = 'patrickomatic') 
        form = JudgeEntrySelectionForm(user = user)
        form_queryset = form.fields['entry'].queryset
        self.assertEqual(len(form_queryset), 1) #There is only one entry in the Imperial Stout category 
        self.assertEqual(form_queryset[0].beer_name, "Musashi's Imperial Stout")

        judge_successful_login = self.client.login(username = 'musashi', password = 'musashi')
        response = self.client.get('/contest/judgeentry')
        user = User.objects.get(username = 'musashi')
        form = JudgeEntrySelectionForm(user = user)
        form_queryset = form.fields['entry'].queryset
        self.assertEqual(len(form_queryset), 2) #There are two entries in the Pale Ale category
        self.assertEqual(form_queryset[0].beer_name, "Patrick's Pale Ale")

    def test_judging_form(self):
        form_data = {
                        u'stylistic_accuracy': [u'1'],
                        u'mouthfeel_score': [u'1'],
                        u'mouthfeel_description': [u'Steel wool'],
                        u'appearance_score': [u'1'],
                        u'overall_impression_score': [u'1'],
                        u'astringent': [u'on'], u'flavor_score': [u'1'],
                        u'technical_merit': [u'1'], u'intangibles': [u'1'],
                        u'flavor_description': [u'Disgusting'],
                        u'acetaldehyde': [u'on'], u'overall_impression_description': [u'Awful'],
                        u'entry': [u'2'], #Entry to be judged
                        u'judge_bjcp_id': [u'121212'],
                        u'aroma_description': [u'Stinky'],
                        u'csrfmiddlewaretoken': [u'ac792da0f7fcf289d807d102da8174c6'],
                        u'aroma_score': [u'1'],
                        u'appearance_description': [u'Nasty']}

        #Style Category: Imperial Stout, judge: patrickomatic
        #Style Category: Pale Ale, judge: musashi

        #Entry #1: Musashi's Imperial Stout
        #Entry #2: Patrick's Pale Ale
        #Entry #3: Musashi's Pale Ale

        #patrickomatic should not be allowed to judge "Patrick's Pale Ale" (Entry #2)
        #because even though he is a judge, he is not a judge for the Pale Ale category.
        form_data['entry'] = 2
        self.client.login(username = 'patrickomatic', password = 'patrickomatic')
        self.assertRaises(RuntimeError, self.client.post, '/contest/judgeentry', form_data)

        #musashi should not be allowed to judge "Musashi's Pale Ale" (Entry #3)
        #because even though he is a judge for the Pale Ale category
        #this would result in him judging his own entry.
        self.client.login(username = 'musashi', password = 'musashi')
        form_data['entry'] = 3 
        self.assertRaises(RuntimeError, self.client.post, '/contest/judgeentry', form_data)

        #Only musashi should be allowed to judge "Patrick's Pale Ale" (Entry #2)
        form_data['entry'] = 2
        self.client.login(username = 'musashi', password = 'musashi')
        self.assertEqual(Entry.objects.get(pk = 2).bjcp_judging_result, None)
        response = self.client.post('/contest/judgeentry', form_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(Entry.objects.get(pk = 2).bjcp_judging_result, None)
