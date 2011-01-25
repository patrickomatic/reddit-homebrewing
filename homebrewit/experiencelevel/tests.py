from django.contrib.auth.models import User
from django.test import TestCase

from homebrewit.experiencelevel.models import *


class ExperienceViewsTest(TestCase):
	fixtures = ['users', 'experiencelevels', 'userexperiencelevels']

	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.client.login(username='patrick', password='password')


	def test_change_level(self):
		response = self.client.get('/experience/level')

		self.assertTemplateUsed(response, 'homebrewit_experience.html')
		self.assert_(response.context['form'])

	def test_change_level__post(self):
		response = self.client.post('/experience/level', {'experience_level': 4})

		self.assertRedirects(response, '/profile/')
		self.assert_(UserExperienceLevel.objects.get(experience_level__id=4, user__id=self.user.id))


	def test_experience_styles(self):
		response = self.client.get('/experience/experience-styles.css')
#		self.assert_('Cache-Control' in str(response))
#		self.assert_('ETag' in str(response))

		content = response.content
		self.assert_('a[href*="user/patrickomatic"]:after' in content)
		self.assert_('a[href*="user/musashiXXX"]:after' in content)
		self.assert_('a[href*="user/loser"]:after' in content)
