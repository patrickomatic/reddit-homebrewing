from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from homebrewit.contest.models import *
from homebrewit.experiencelevel.models import *
from homebrewit.signup.models import UserProfile


def profile(request, user):
	level_image = None

	try:
		level = UserExperienceLevel.objects.get(user__id=request.user.id)
		level_image = level.experience_level.img_url
	except UserExperienceLevel.DoesNotExist:
		level = None

	contest_entries = Entry.objects.filter(user=user)

	is_profile_owner = request.user.is_authenticated() and user.username == request.user.username

	return render_to_response('homebrewit_profile.html', {'user': user,
                'level': level, 'contest_entries': contest_entries, 
                'is_profile_owner': is_profile_owner, 
				'level_image': level_image},
		context_instance=RequestContext(request))


def anonymous_profile(request, username):
	try:
		return profile(request, User.objects.get(username=username))
	except User.DoesNotExist:
		raise Http404


@login_required
def logged_in_profile(request):
	return profile(request, request.user)


class AddressForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)

class EmailForm(forms.Form):
	email = forms.EmailField()

@login_required
def edit_profile(request):
	try:
		profile = request.user.get_profile()
	except UserProfile.DoesNotExist:
		profile = None


	if request.method == 'POST':
		address_form = AddressForm(request.POST, instance=profile)
		email_form = EmailForm(request.POST)

		if email_form.is_valid() and address_form.is_valid():
			# save the UserProfile object
			profile = address_form.save(commit=False)
			profile.user = request.user
			profile.save()

			# and now save the email
			request.user.email = email_form.cleaned_data['email']
			request.user.save()

			request.user.message_set.create(message='Successfully set address info.')
	else:
		address_form = AddressForm(instance=profile)
		email_form = EmailForm(initial={'email': request.user.email})


	return render_to_response('homebrewit_edit_profile.html', 
			{'address_form': address_form, 'email_form': email_form},
			context_instance=RequestContext(request))
