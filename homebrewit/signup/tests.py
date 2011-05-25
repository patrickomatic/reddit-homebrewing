import datetime, reddit
from django.contrib.auth.models import User
from django.test import TestCase


class SignupViewsTest(TestCase):
	fixtures = ['beerstyles', 'entries', 'judgingresults', 'users']

	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.client.login(username=self.user.username, password='password')


	def test_index(self):
		self.client.logout()
		response = self.client.get('/')

		self.assertTemplateUsed(response, 'homebrewit_index.html')
		self.assert_(len(response.context['contest_data']) == 1)
		self.assert_(len(response.context['contest_data'][2011]) == 8)
		self.assert_(response.context['current_year'] == datetime.datetime.now().year)
		self.assert_(response.context['login_form'])

	def test_index__post(self):
# XXX have to mock out reddit to call this
#		self.client.logout()
#		response = self.client.post('/', 
#				{'reddit_username': self.user.username, 'password': 'password'})
#
#		self.assertRedirects(response, '/profile')
#		self.assert_(self.user.is_authenticated())
		pass


	def test_logout(self):
		response = self.client.get('/logout')
		self.assertRedirects(response, '/')


# XXX we're not using the verify_token_in_thread method for authentication
# any more
#class RedditTest(TestCase):
#	def test_verify_token_in_thread(self):
#		self.assert_(reddit.verify_token_in_thread("http://www.reddit.com/r/Homebrewing/comments/ghqbs/how_do_different_yeast_strains_affect_brews/", "arcsine", "Woot! I just recovered some Gulden Draak yeast, good to know it wasn't already commercially available. Thanks!"))
#
#	def test_verify_token_in_thread__wrongToken(self):
#		self.assert_(not reddit.verify_token_in_thread("http://www.reddit.com/r/Homebrewing/comments/ghqbs/how_do_different_yeast_strains_affect_brews/", "802bikeguy_com", "wrongtoken"))
#
#	def test_verify_token_in_thread__otherUser(self):
#		self.assert_(not reddit.verify_token_in_thread("http://www.reddit.com/r/Homebrewing/comments/ghqbs/how_do_different_yeast_strains_affect_brews/", "802bikeguy_com", "Woot! I just recovered some Gulden Draak yeast, good to know it wasn't already commercially available. Thanks!"))
