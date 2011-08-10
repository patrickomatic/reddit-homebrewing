import datetime 

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import simplejson as json

from homebrewit import reddit
from homebrewit.experiencelevel.models import *


class MockResponse:
	def __init__(self, resp_data, code=200, msg='OK'):
		self.resp_data = resp_data
		self.code = code
		self.msg = msg
		self.headers = {'content-type': 'application/json'}

	def read(self):
		return self.resp_data

	def getcode(self):
		return self.code


class SignupViewsTest(TestCase):
	fixtures = ['beerstyles', 'contestyears', 'entries', 'judgingresults', 'users']

	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.client.login(username=self.user.username, password='password')
		self.saved_urlopen = reddit.urllib2.urlopen

	def tearDown(self):
		reddit.urllib2.urlopen = self.saved_urlopen


	def test_index(self):
		self.client.logout()
		response = self.client.get('/')

		self.assertTemplateUsed(response, 'homebrewit_index.html')
		self.assert_(len(response.context['contest_data']) == 1)
		self.assert_(len(response.context['contest_data'][2011]) == 8)
		self.assert_(response.context['current_year'] == datetime.datetime.now().year)
		self.assert_(response.context['login_form'])

	def test_index__post_first_time(self):
		def urlopen_mock(request):
			return MockResponse(json.dumps({"json": {"errors": [], "data": {"modhash": "t0t0t0", "cookie": "1234567,..."}}}))
		reddit.urllib2.urlopen = urlopen_mock

		self.client.logout()

		response = self.client.post('/', {'username': self.user.username, 'password': 'password'})

		self.assertRedirects(response, '/profile/')
		self.assert_(self.user.is_authenticated())

	def test_index__post_after_user_is_created(self):
		self.client.logout()
		response = self.client.post('/', {'username': self.user.username, 'password': 'password'})

		self.assertRedirects(response, '/profile/')
		self.assert_(self.user.is_authenticated())


	def test_logout(self):
		response = self.client.get('/logout')
		self.assertRedirects(response, '/')


	def test_related_reddits(self):
		response = self.client.get('/related')
		self.assertTemplateUsed(response, 'homebrewit_related_reddits.html')


class RedditTest(TestCase):
	fixtures = ['experiencelevels', 'users', 'userexperiencelevels']


	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.saved_urlopen = reddit.urllib2.urlopen

	def tearDown(self):
		reddit.urllib2.urlopen = self.saved_urlopen


	def test_reddit_login(self):
		def urlopen_mock(request):
			self.assert_(request.get_full_url() == 'http://www.reddit.com/api/login/patrickomatic')
			data = request.get_data()
			self.assert_(not 'uh' in data)
			self.assert_('passwd=password' in data)
			self.assert_('user=patrickomatic' in data)
			self.assert_('api_type=json' in data)
			self.assert_(request.has_header('User-agent'))

			return MockResponse(json.dumps({"json": {"errors": [], "data": {"modhash": "t0t0t0", "cookie": "1234567,..."}}}))

		reddit.urllib2.urlopen = urlopen_mock
		
		session = reddit.reddit_login('patrickomatic', 'password')
		self.assert_(session)
		self.assert_(session.modhash == 't0t0t0')
		self.assert_(not session.has_been_used)

	def test_reddit_login__failure(self):
		def urlopen_mock(request):
			return MockResponse(json.dumps({"json": {"errors": [["WRONG PASSWORD", "invalid password"]]}}))

		reddit.urllib2.urlopen = urlopen_mock
		
		self.assert_(reddit.reddit_login('patrickomatic', 'foo') is None)


	def test_can_reddit_login(self):
		def urlopen_mock(request):
			return MockResponse(json.dumps({"json": {"errors": [], "data": {"modhash": "t0t0t0", "cookie": "1234567,..."}}}))
		reddit.urllib2.urlopen = urlopen_mock

		self.assert_(reddit.reddit_login('patrickomatic', 'password'))


	def test_set_flair(self):
		session = reddit.RedditSession(modhash='t0t0t0')

		def urlopen_mock(request):
			self.assert_(request.get_full_url() == 'http://www.reddit.com/api/flair')
			data = request.get_data()
			self.assert_('uh=t0t0t0' in data)
			self.assert_('r=homebrewing' in data)
			self.assert_('name=patrick' in data)
			self.assert_('css_class=advanced' in data)
			self.assert_(request.has_header('User-agent'))

			return MockResponse("")

		reddit.urllib2.urlopen = urlopen_mock
		reddit.set_flair(UserExperienceLevel(user=self.user, experience_level=ExperienceLevel.objects.get(pk=3)), session)

		self.assert_(session.has_been_used)


	def test_retry(self):
			times_called = [0]

			@reddit.retry(5, ValueError)
			def retry_tester():
					times_called[0] += 1
					raise ValueError("success")

			self.assertRaises(ValueError, retry_tester)
			self.assert_(times_called[0] == 5)

	def test_retry__eventually_succeed(self):
			times_called = [0]

			@reddit.retry(5, Exception)
			def retry_tester():
					times_called[0] += 1
					if times_called[0] < 3:
							raise Exception

					return "success"

			self.assert_("success" == retry_tester())
			self.assert_(times_called[0] == 3)


#	def test_verify_token_in_thread(self):
#		self.assert_(reddit.verify_token_in_thread("http://www.reddit.com/r/Homebrewing/comments/ghqbs/how_do_different_yeast_strains_affect_brews/", "arcsine", "Woot! I just recovered some Gulden Draak yeast, good to know it wasn't already commercially available. Thanks!"))
#
#	def test_verify_token_in_thread__wrongToken(self):
#		self.assert_(not reddit.verify_token_in_thread("http://www.reddit.com/r/Homebrewing/comments/ghqbs/how_do_different_yeast_strains_affect_brews/", "802bikeguy_com", "wrongtoken"))
#
#	def test_verify_token_in_thread__otherUser(self):
#		self.assert_(not reddit.verify_token_in_thread("http://www.reddit.com/r/Homebrewing/comments/ghqbs/how_do_different_yeast_strains_affect_brews/", "802bikeguy_com", "Woot! I just recovered some Gulden Draak yeast, good to know it wasn't already commercially available. Thanks!"))
