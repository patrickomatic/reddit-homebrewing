from django.contrib.auth.models import User
from django.test import TestCase

from homebrewit.experiencelevel.models import *


class ProfileViewsTest(TestCase):
	fixtures = ['users']

	def setUp(self):
		self.user = User.objects.get(username='patrick')


	def test_anonymous_profile(self):
		response = self.client.get('/profile/%s' % self.user.username)

		self.assertTemplateUsed(response, 'homebrewit_profile.html')
		self.assert_(not response.context['is_profile_owner'])
		self.assert_(response.context['user'] == self.user)
		self.assert_(len(response.context['contest_entries']) == 0)

	def test_anonymous_profile__404(self):
		response = self.client.get('/profile/doesntexist')
		self.assert_(response.status_code == 404)


	def test_logged_in_profile(self):
		self.client.login(username=self.user.username, password='password')
		response = self.client.get('/profile/')

		self.assertTemplateUsed(response, 'homebrewit_profile.html')
		self.assert_(response.context['level'] is None)
		self.assert_(len(response.context['contest_entries']) == 0)
		self.assert_(response.context['is_profile_owner'])
		self.assert_(response.context['user'] == self.user)
