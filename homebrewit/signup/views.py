from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
	return render_to_response('homebrewit_index.html', {}, 
			context_instance=RequestContext(request))

class SignupForm(forms.Form):
	reddit_username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField()
	# XXX address


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			# XXX reddit has an api for validating username/password
			user = User.objects.create_user(form.cleaned_data['reddit_username'], form.cleaned_data['email'], form.cleaned_data['password'])
			user = authenticate(username=form.cleaned_data['reddit_username'], password=form.cleaned_data['password'])
			user.save()
			auth_login(request, user)

			request.user.message_set.create(message='You have successfully signed up')
			return HttpResponseRedirect('/profile')
	else:
		form = SignupForm()

	return render_to_response('homebrewit_signup.html', {'form': form},
			context_instance=RequestContext(request))


class LoginForm(forms.Form):
	reddit_username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput())

def login(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['reddit_username'], password=form.cleaned_data['password'])
			auth_login(request, user)
			return HttpResponseRedirect('/profile')
	else:
		form = SignupForm()

	return render_to_response('homebrewit_login.html', {'form': form},
			context_instance=RequestContext(request))


@login_required
def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/")
	

@login_required
def dashboard(request):
	return render_to_response('homebrewit_dashboard.html', {},
			context_instance=RequestContext(request))
