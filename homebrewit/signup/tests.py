import datetime
from django.contrib.auth.models import User
from django.test import TestCase


class SignupViewsTest(TestCase):
	fixtures = ['beerstyles', 'users']

	def setUp(self):
		self.user = User.objects.get(username='patrick')
		self.client.login(username=self.user.username, password='password')


	def test_index(self):
		self.client.logout()
		response = self.client.get('/')

		self.assertTemplateUsed(response, 'homebrewit_index.html')
		self.assert_(response.context['years'] == [2011])
		self.assert_(response.context['current_year'] == datetime.datetime.now().year)


	def test_signup(self):
		self.client.logout()
		response = self.client.get('/signup')

		self.assertTemplateUsed(response, 'homebrewit_signup.html')
		self.assert_(response.context['address_form'])
		self.assert_(response.context['signup_form'])

	def test_signup__post(self):
		self.client.logout()
		# XXX have to mock out call to reddit
	
	def test_signup__post_with_address_form(self):
		self.client.logout()
		# XXX have to mock out call to reddit

	def test_signup__post_with_bad_address_form(self):
		self.client.logout()
		# XXX have to mock out call to reddit


	def test_login(self):
		response = self.client.get('/login')

		self.assertTemplateUsed(response, 'homebrewit_login.html')
		self.assert_(response.context['form'])

	def test_login__post(self):
		self.client.logout()
		response = self.client.post('/login', 
				{'username': self.user.username, 'password': 'password'})

		self.assertTemplateUsed(response, 'homebrewit_login.html')
		self.assert_(self.user.is_authenticated())


	def test_logout(self):
		response = self.client.get('/logout')
#		self.assert_(not user.is_authenticated())  # XXX why not?
		self.assertRedirects(response, '/')
