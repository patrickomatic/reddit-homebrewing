from django.contrib.auth.models import User
from django.test import TestCase

from homebrewit.experiencelevel.models import *
from homebrewit.signup.models import UserProfile


class ProfileViewsTest(TestCase):
    fixtures = ['users', 'contestyears']

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
        self.assert_(response.context['contest_year'].contest_year == 2011)


    def test_edit_profile(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.get('/profile/edit')

        self.assertTemplateUsed(response, 'homebrewit_edit_profile.html')
        self.assert_(response.context['address_form'])
        self.assert_(response.context['email_form'])

    def test_edit_profile__post(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post('/profile/edit',
                {'email': 'patrick@patrickomatic.com', 
                    'address_1': '128 Hilltop Rd', 'city': 'Silver Spring',
                    'state': 'MD', 'country': 'United States', 
                    'zip_code': '20910'})

        self.assertTemplateUsed(response, 'homebrewit_edit_profile.html')

        profile = UserProfile.objects.get(user__id=self.user.id)
        self.assert_(self.user.email == 'patrick@patrickomatic.com')
        self.assert_(profile.address_1 == '128 Hilltop Rd')
        self.assert_(profile.country == 'United States')


    def test_change_password(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.get('/profile/password')

        self.assertTemplateUsed(response, 'homebrewit_change_password.html')
        self.assert_(response.context['form'])

    def test_change_password__post(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post('/profile/password', 
                {'old_password': 'password', 'new_password1': 'foo',
                    'new_password2': 'foo'})
        self.assertRedirects(response, '/profile/edit')
        self.assert_(self.client.login(username=self.user.username, password='foo'))
