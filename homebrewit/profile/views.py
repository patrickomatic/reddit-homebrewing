import logging

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.base import *

from homebrewit.contest.models import *
from homebrewit.experiencelevel.models import *
from homebrewit.signup.models import UserProfile

logger = logging.getLogger(__name__)


class ProfileView(TemplateView):
    template_name = "profile/profile.html"

    def get_context_data(self, **kwargs):
        level_image = None

        if kwargs.get('username'):
            user = User.objects.get(username=kwargs['username'])
        else:
            user = self.request.user

        try:
            level = UserExperienceLevel.objects.get(user__id=self.request.user.id)
            level_image = level.experience_level.img_url
        except UserExperienceLevel.DoesNotExist:
            level = None

        contest_entries = Entry.objects.filter(user=user)

        is_profile_owner = self.request.user.is_authenticated() and user.username == self.request.user.username

        return {
            'profile_user': user,
            'level': level, 
            'contest_entries': contest_entries, 
            'is_profile_owner': is_profile_owner, 
            'level_image': level_image,
            'contest_year': ContestYear.objects.get_current_contest_year(),
        }


class AddressForm(forms.ModelForm):
    next = forms.CharField(max_length=1025, widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput,
            'address_1': forms.TextInput,
            'address_2': forms.TextInput,
            'city': forms.TextInput,
            'state': forms.TextInput,
            'zip_code': forms.TextInput,
            'country': forms.TextInput,
        }
 
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
        address_form = AddressForm(initial={'next': request.GET.get('next')}, instance=profile)
        email_form = EmailForm(initial={'email': request.user.email})


    return render(request, 'profile/edit.html', {
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

    return render(request, 'profile/change_password.html', {'form': form})
