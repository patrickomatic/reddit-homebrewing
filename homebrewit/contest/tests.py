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
		response = self.client.get('/contest/styles')
		self.assertTemplateUsed(response, 'homebrewit_contest_styles.html')


	def test_contest_year(self):
		response = self.client.get('/contest/2010/')
		self.assertTemplateUsed(response, 'homebrewit_contest_year.html')


	def test_entry(self):
		#response = self.client.get('/contest/entries/
		pass

	
	def test_winner_styles(self):
		pass


class JudgeContestCommandTest(TestCase):
	fixtures = ['beerstyles']

	def test_handle(self):
		# XXX
		pass
