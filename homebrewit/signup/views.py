import hashlib, random

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



def index(request):
    # if it's a login...
    if request.method == 'POST':
        login_form = RedditAuthenticationForm(data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return HttpResponseRedirect('/profile/')
    else:
        login_form = RedditAuthenticationForm()

    # XXX this is a lot of stuff to have in a controller
    # get each years beer styles
    contest_data = {} 
    for style in BeerStyle.objects.all():
        year = style.contest_year.contest_year

        top_entry = Entry.objects.get_top_n(style, 1)
        if top_entry and top_entry[0].winner:
            winner_data = {
                    'winner': top_entry[0].user.username + ": " + unicode(top_entry[0].score),
                    'id': top_entry[0].id,
                    }
        else:
            winner_data = None

        data = {
                'n_entries': Entry.objects.filter(style=style).count(),
                'n_judged': Entry.objects.filter(style=style, score__isnull=False).count(),
                'n_received': Entry.objects.filter(style=style, received_entry=True).count(),
                'winner': winner_data,
                'style': style,
                }

        if year in contest_data:
            contest_data[year].append(data)
        else:
            contest_data[year] = [data]


    return render(request, 'homebrewit_index.html', {
        'contest_data': [(year, contest_data[year]) for year in sorted(contest_data.iterkeys(), reverse=True)], 
        'contest_year': ContestYear.objects.get_current_contest_year(),
        'login_form': login_form,
        })


def signup(request):
    if request.method == 'POST':
        signup_form = RedditCommentTokenUserCreationForm(request.POST)

        if signup_form.is_valid():
            user = signup_form.save()

            user = authenticate(username=signup_form.cleaned_data['username'],
                    password=signup_form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Successfully verified your reddit account.')

            return HttpResponseRedirect('/profile/%s' % user.username)
    else:
        signup_form = RedditCommentTokenUserCreationForm()

    return render(request, 'homebrewit_signup.html', {
        'signup_form': signup_form,
        'registration_thread': settings.REDDIT_REGISTRATION_THREAD,
    })


def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)

    return HttpResponseRedirect("/")
