import datetime

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from homebrewit.contest.models import BeerStyle, Entry 
from homebrewit.signup.reddit import reddit_login


class LoginForm(forms.Form):
	reddit_username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput())


	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(LoginForm, self).__init__(*args, **kwargs)


	def clean(self):
#		if not reddit_login(self.cleaned_data.get('reddit_username'), 
#				self.cleaned_data.get('password')):
#			raise forms.ValidationError('The supplied username and password don\'t work on reddit.com')

		try:
			user = User.objects.get(username=self.cleaned_data['reddit_username'])
		except User.DoesNotExist:
			user = User.objects.create_user(self.cleaned_data['reddit_username'], '', self.cleaned_data['password'])
			
		user = authenticate(username=user.username, 
					password=self.cleaned_data['password'])

		if not user.is_authenticated():
			# wtf... the only way they could be not be authenticated here
			# is if they changed their password on reddit. i think...
			user.password = self.cleaned_data['password']
			user.save()
			user = authenticate(username=user.username, password=user.password)

		auth_login(self.request, user)

		return self.cleaned_data
	
def index(request):
	contest_data, login_form = {}, LoginForm(request=request)

	# if it's a login...
	if request.method == 'POST':
		login_form = LoginForm(request.POST, request=request)
		if login_form.is_valid():
			return HttpResponseRedirect('/profile')

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

	return render_to_response('homebrewit_index.html', 
			{
				'contest_data': contest_data, 
				'current_year': datetime.datetime.now().year,
				'login_form': login_form,
			}, context_instance=RequestContext(request))


def logout(request):
	if request.user.is_authenticated():
		auth_logout(request)

	return HttpResponseRedirect("/")
