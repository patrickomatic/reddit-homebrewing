from django.contrib.auth.models import User
from django.test import TestCase

from homebrewit.contest.management.commands import *
from homebrewit.contest.models import *
from homebrewit.contest.views import *


class ContestViewsTest(TestCase):
	fixtures = ['beerstyles']

	def setUp(self):
		self.user = User.objects.create_user('patrick', 'patrick@patrickomatic.com', 'pass')
		self.client.login(username=self.user.username, password='pass')


	def test_register(self):
		response = self.client.get('/contest/register')
		self.assert_(response.context['form'])

	def test_register__post(self):
		pass
#		response = self.client.post('/contest/register', {'


	def test_styles(self):
		response = self.client.get('/contest/2011/styles')
		self.assertTemplateUsed(response, 'homebrewit_contest_styles.html')


	def test_contest_year(self):
		response = self.client.get('/contest/2011/')
		self.assertTemplateUsed(response, 'homebrewit_contest_year.html')


	def test_entry(self):
		#response = self.client.get('/contest/entries/
		pass

	
	def test_winner_styles(self):
		pass


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
