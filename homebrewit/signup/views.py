import datetime, hashlib, random

from django import forms
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from homebrewit.contest.models import BeerStyle, Entry 
from homebrewit.signup import secret_key
from homebrewit.signup.reddit import verify_token_in_thread


def index(request):
	# if it's a login...
	if request.method == 'POST':
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			login(request, login_form.get_user())
			return HttpResponseRedirect('/profile')
	else:
		login_form = AuthenticationForm()

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
				'winner': winner_data,
				'style': style,
		}

		if year in contest_data:
			contest_data[year].append(data)
		else:
			contest_data[year] = [data]

	return render_to_response('homebrewit_index.html', {
				'contest_data': contest_data, 
				'current_year': datetime.datetime.now().year,
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
		if not verify_token_in_thread(settings.REDDIT_REGISTRATION_THREAD,
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
