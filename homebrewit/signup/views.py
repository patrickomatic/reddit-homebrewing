import hashlib, random

from django import forms
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from homebrewit.contest.models import BeerStyle, ContestYear, Entry 
from homebrewit.signup import secret_key
from homebrewit.reddit import can_reddit_login, verify_token_in_thread


class RedditAuthenticationForm(AuthenticationForm):
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		# if the user already exists, just go straight through with login
		if username and password:
			try:
				User.objects.get(username=username)
			except User.DoesNotExist:
				if not can_reddit_login(username, password):
					raise forms.ValidationError("This username and password don't seem to work on reddit")

				# ok they authenticate on reddit - create them
				User.objects.create_user(username, '', password)

		super(RedditAuthenticationForm, self).clean()

		return self.cleaned_data


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

		top_entry = Entry.objects.filter(style=style).order_by('-score')
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

	return render_to_response('homebrewit_index.html', {
				'contest_data': contest_data, 
				'contest_year': ContestYear.objects.get_current_contest_year(),
				'login_form': login_form,
		}, context_instance=RequestContext(request))


class RedditCommentTokenUserCreationForm(UserCreationForm):
	token = forms.CharField(max_length=64)
	signature = forms.CharField(max_length=512, widget=forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Reddit Username'
		token = hashlib.sha256(str(random.random())).hexdigest()
		self.initial = {'token': token, 'signature': self.__sign(token)}

	def clean(self):
		# check that the token and signature still match (i.e. the token 
		# hasn't been changed)
		data = self.cleaned_data
		if data['signature'] != self.__sign(data['token']):
			raise forms.ValidationError('Session forgery detected.  Please refresh the page and try again.')

		# now verify they posted the given token as the correct user
		if not verify_token_in_thread(settings.REDDIT_REGISTRATION_THREAD_JSON,
				data['username'], data['token']):
			raise forms.ValidationError('Unable to verify that you posted the token.  Please go to the included link and post the given token before submitting this form.')

		return data

	def __sign(self, token):
		return hashlib.sha256(token + secret_key).hexdigest()


def signup(request):
	if request.method == 'POST':
		signup_form = RedditCommentTokenUserCreationForm(request.POST)

		if signup_form.is_valid():
			user = signup_form.save()

			user = authenticate(username=signup_form.cleaned_data['username'],
					password=signup_form.cleaned_data['password1'])
			login(request, user)
			user.message_set.create(message='Successfully verified your reddit account.')
				
			return HttpResponseRedirect('/profile/%s' % user.username)
	else:
		signup_form = RedditCommentTokenUserCreationForm()

	return render_to_response('homebrewit_signup.html', {
				'signup_form': signup_form,
				'registration_thread': settings.REDDIT_REGISTRATION_THREAD,
		}, context_instance=RequestContext(request))
	

def logout(request):
	if request.user.is_authenticated():
		auth_logout(request)

	return HttpResponseRedirect("/")


def related_reddits(request):
    return render_to_response('homebrewit_related_reddits.html', {}, 
			context_instance=RequestContext(request))
