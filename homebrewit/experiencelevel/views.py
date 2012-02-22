import datetime, urllib2

from django import forms
from django.core.mail import mail_admins
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from homebrewit.experiencelevel.models import *
from homebrewit.reddit import set_flair, reddit_login


class ExperienceForm(forms.Form):
	experience_level = forms.ModelChoiceField(queryset=ExperienceLevel.objects.all())

@login_required
def change_level(request):
	try:
		level = UserExperienceLevel.objects.get(user__id=request.user.id)
		initial = {'experience_level': level.experience_level}
	except UserExperienceLevel.DoesNotExist:
		level = None
		initial = {}

	if request.method == 'POST':
		form = ExperienceForm(request.POST, initial=initial)

		if form.is_valid():
			data = form.cleaned_data

			if level:
				level.experience_level = data['experience_level']
			else:
				level = UserExperienceLevel(experience_level=data['experience_level'], user=request.user)
			level.save()

			try:
				set_flair(level)
				request.user.message_set.create(message='Successfully set experience level to %s.' % level.experience_level)
				return HttpResponseRedirect('/profile/')
			except urllib2.HTTPError:
				request.user.message_set.create(message='Whoops! There was an error setting your experience level.  This usually happens when reddit\'s API is down.  Try again later and if you continue to have problems, please contact the moderators.')
	else:
		form = ExperienceForm(initial=initial)
		
	return render_to_response('homebrewit_experience.html', {'form': form},
			context_instance=RequestContext(request))


def experience_styles(request):
	return render_to_response('experience_styles.css',
			{'experience_levels': UserExperienceLevel.objects.all()},
			mimetype='text/css')

