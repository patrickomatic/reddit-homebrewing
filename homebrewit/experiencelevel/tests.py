import urllib2

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import simplejson as json

from homebrewit.experiencelevel.models import *
from homebrewit import reddit
from homebrewit.signup.tests import MockResponse


class ExperienceViewsTest(TestCase):
	fixtures = ['users', 'experiencelevels', 'userexperiencelevels', 'contestyears']

	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.client.login(username='patrick', password='password')
		self.saved_urlopen = reddit.urllib2.urlopen
		settings.MODERATOR_USERNAME = 'patrick'
		settings.MODERATOR_PASSWORD = 'password'

		self.urlopen_mock = lambda req: MockResponse(json.dumps({"json": {"errors": [], "data": {"modhash": "t0t0t0", "cookie": "1234567,..."}}}))


	def tearDown(self):
		reddit.urllib2.urlopen = self.saved_urlopen


	def test_change_level(self):
		response = self.client.get('/experience/level')

		self.assertTemplateUsed(response, 'homebrewit_experience.html')
		self.assert_(response.context['form'])

	def test_change_level__post(self):
		reddit.urllib2.urlopen = self.urlopen_mock

		response = self.client.post('/experience/level', {'experience_level': 4})

		self.assertRedirects(response, '/profile/')
		self.assert_(UserExperienceLevel.objects.get(experience_level__id=4, user__id=self.user.id))

	def test_change_level__json_post(self):
		reddit.urllib2.urlopen = self.urlopen_mock
		
		response = self.client.post('/experience/level', {'experience_level': 4}, HTTP_ACCEPT='application/json')
		self.assert_(UserExperienceLevel.objects.get(experience_level__id=4, user__id=self.user.id))

		assert response['Content-Type'] == 'application/json'
		assert '"success": true' in response.content
		assert '"message":' in response.content

	def test_change_level__reddit_api_down(self):
		def urlopen_mock(request):
			raise urllib2.HTTPError("foo", "bar", None, None, None)

		reddit.urllib2.urlopen = urlopen_mock

		response = self.client.post('/experience/level', {'experience_level': 4})

		self.assertTemplateUsed(response, 'homebrewit_experience.html')

		# this is a little awkward because you have to iterate through a message_set
		saw_error = False
		for message in response.context['messages']:
			if u'Whoops!' in unicode(message):
				saw_error = True
				break

		self.assert_(saw_error)
		self.assert_(response.context['form'])


	def test_experience_styles(self):
		response = self.client.get('/experience/experience-styles.css')

		content = response.content
		self.assert_('a[href*="user/patrickomatic"]:after' in content)
		self.assert_('a[href*="user/musashiXXX"]:after' in content)
		self.assert_('a[href*="user/loser"]:after' in content)
