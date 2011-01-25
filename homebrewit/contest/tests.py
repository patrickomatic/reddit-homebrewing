from django.contrib.auth.models import User
from django.test import TestCase

from homebrewit.contest.management.commands import *
from homebrewit.contest.models import *
from homebrewit.contest.views import *


class ContestViewsTest(TestCase):
	fixtures = ['beerstyles', 'entries', 'users', 'judgingresults']

	def setUp(self):
		self.client.login(username='patrick', password='password')


	def test_register(self):
		response = self.client.get('/contest/register')
		self.assert_(response.context['form'])

	def test_register__post(self):
		response = self.client.post('/contest/register', {'beer_name': "Patrick's super skunky IPA", 'style': '1'})
		entry = Entry.objects.get(beer_name="Patrick's super skunky IPA")
		self.assert_(entry.user.username == 'patrick')


	def test_contest_year(self):
		response = self.client.get('/contest/2011/')
		self.assertTemplateUsed(response, 'homebrewit_contest_year.html')


	def test_entry(self):
		#response = self.client.get('/contest/entries/
		pass


	def test_style(self):
		pass

	
	def test_winner_styles(self):
		response = self.client.get('/contest/winner-styles.css')
#		self.assert_('Cache-Control' in str(response))
#		self.assert_('ETag' in str(response))

		content = response.content
		self.assert_('a[href*="user/patrickomatic"]:after' in content)
		self.assert_('a[href*="user/musashiXXX"]:after' in content)
		self.assert_(not 'a[href*="user/loser"]:after' in content)


class ContestModelsTest(TestCase):
	fixtures = ['beerstyles', 'entries', 'users', 'judgingresults']

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


class JudgeContestCommandTest(TestCase):
	fixtures = ['beerstyles']

	def test_handle(self):
		# XXX
		pass
