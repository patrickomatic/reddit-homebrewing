from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import simplejson as json

from homebrewit.experiencelevel.models import *
from homebrewit import reddit
from homebrewit.signup.tests import MockResponse


class ExperienceViewsTest(TestCase):
	fixtures = ['users', 'experiencelevels', 'userexperiencelevels']

	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.client.login(username='patrick', password='password')
		self.saved_urlopen = reddit.urllib2.urlopen

	def tearDown(self):
		reddit.urllib2.urlopen = self.saved_urlopen


	def test_change_level(self):
		response = self.client.get('/experience/level')

		self.assertTemplateUsed(response, 'homebrewit_experience.html')
		self.assert_(response.context['form'])

	def test_change_level__post(self):
		def urlopen_mock(request):
			return MockResponse(json.dumps({"json": {"errors": [], "data": {"modhash": "t0t0t0", "cookie": "1234567,..."}}}))
		reddit.urllib2.urlopen = urlopen_mock

		response = self.client.post('/experience/level', {'experience_level': 4, 'reddit_password': 'password'})

		self.assertRedirects(response, '/profile/')
		self.assert_(UserExperienceLevel.objects.get(experience_level__id=4, user__id=self.user.id))

	def test_change_level__post_no_password(self):
		response = self.client.post('/experience/level', {'experience_level': 4})

		self.assert_(response.context['form'].errors)


	def test_experience_styles(self):
		response = self.client.get('/experience/experience-styles.css')

		content = response.content
		self.assert_('a[href*="user/patrickomatic"]:after' in content)
		self.assert_('a[href*="user/musashiXXX"]:after' in content)
		self.assert_('a[href*="user/loser"]:after' in content)
