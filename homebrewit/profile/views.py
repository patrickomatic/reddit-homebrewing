from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
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

    return render(request, 'homebrewit_profile.html', {
                'user': user,
                'level': level, 
                'contest_entries': contest_entries, 
                'is_profile_owner': is_profile_owner, 
                'level_image': level_image,
                'contest_year': ContestYear.objects.get_current_contest_year(),
            })


def anonymous_profile(request, username):
    try:
        return profile(request, User.objects.get(username=username))
    except User.DoesNotExist:
        raise Http404


@login_required
def logged_in_profile(request):
    return profile(request, request.user)


class AddressForm(forms.ModelForm):
    next = forms.CharField(max_length=1025, widget=forms.HiddenInput(), required=False)

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

            messages.success(request, 'Successfully set address info.')
            if address_form.cleaned_data.get('next'):
                return HttpResponseRedirect(address_form.cleaned_data['next'])
    else:
        # pass GET because it might have a next
        address_form = AddressForm(initial={'next': request.GET.get('next')},
                instance=profile)
        email_form = EmailForm(initial={'email': request.user.email})


    return render(request, 'homebrewit_edit_profile.html', {
                'address_form': address_form, 
                'email_form': email_form,
            })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully set password')
            return HttpResponseRedirect('/profile/edit')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'homebrewit_change_password.html', {'form': form})
