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

from homebrewit.contest.models import BeerStyle, ContestYear
from homebrewit.signup.reddit import reddit_login
from homebrewit.signup.models import UserProfile


def index(request):
	return render_to_response('homebrewit_index.html', 
			{'years': [y.contest_year for y in ContestYear.objects.all()], 
				'current_year': datetime.datetime.now().year}, 
			context_instance=RequestContext(request))


class SignupForm(forms.Form):
	reddit_username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField()

	def clean(self):
		try:
			User.objects.get(username=self.cleaned_data['reddit_username'])
			raise forms.ValidationError('The given username already exists')
		except User.DoesNotExist:
			pass

		if not reddit_login(self.cleaned_data['reddit_username'], self.cleaned_data['password']):
			raise forms.ValidationError('The supplied username and password don\'t work on reddit.com')

		return self.cleaned_data
	

class AddressForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)


def create_user(email, username, password, profile=None):
	user = User.objects.create_user(username, email, password)
	user.save()

	if profile:
		profile.user = user
		profile.save()

	return authenticate(username=username, password=password)


def signup(request):
	if request.method == 'POST':
		signup_form, address_form = SignupForm(request.POST), AddressForm(request.POST)

		if signup_form.is_valid():
			submitted_address_form = False
			for label in address_form:
				if label.html_name in request.POST:
					submitted_address_form = True
					break
				
			user = None
			if submitted_address_form and address_form.is_valid():
				user = create_user(signup_form.cleaned_data['email'],
						signup_form.cleaned_data['reddit_username'],
						signup_form.cleaned_data['password'],
						address_form.save(commit=False))
			elif not submitted_address_form:
				user = create_user(signup_form.cleaned_data['email'],
						signup_form.cleaned_data['reddit_username'], 
						signup_form.cleaned_data['password']) 

			if user:
				auth_login(request, user)

				request.user.message_set.create(message='You have successfully signed up')
				return HttpResponseRedirect('/profile')
	else:
		signup_form, address_form = SignupForm(), AddressForm()


	return render_to_response('homebrewit_signup.html', 
			{'signup_form': signup_form, 'address_form': address_form},
			context_instance=RequestContext(request))


class LoginForm(forms.Form):
	reddit_username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput())

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['reddit_username'], password=form.cleaned_data['password'])
			auth_login(request, user)
			return HttpResponseRedirect('/profile')
	else:
		form = LoginForm()

	return render_to_response('homebrewit_login.html', {'form': form},
			context_instance=RequestContext(request))


@login_required
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/")
