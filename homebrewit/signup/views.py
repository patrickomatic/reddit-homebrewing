import hashlib, random, logging

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from homebrewit.contest.models import BeerStyle, ContestYear, Entry 
from homebrewit.signup import secret_key
from homebrewit.reddit import *


logger = logging.getLogger(__name__)


class RedditAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not authenticate(username=username, password=password) and can_reddit_login(username, password): 
            self.__create_or_update_password(username, password)

        return super(RedditAuthenticationForm, self).clean() 

    def __create_or_update_password(self, username, password):
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
        except User.DoesNotExist:
            User.objects.create_user(username, '', password)


# XXX This probably makes more sense in contest.views
def index(request):
    if request.method == 'POST':
        login_form = RedditAuthenticationForm(data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return HttpResponseRedirect('/profile/')
    else:
        login_form = RedditAuthenticationForm()

    return render(request, 'homebrewit_index.html', {
        'contest_data': ContestYear.objects.get_all_year_summary(), 
        'contest_year': ContestYear.objects.get_current_contest_year(),
        'login_form': login_form,
    })


def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)

    return HttpResponseRedirect("/")
