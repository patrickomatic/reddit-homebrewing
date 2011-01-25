from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from homebrewit.experiencelevel.models import *


class ExperienceForm(forms.Form):
	experience_level = forms.ModelChoiceField(queryset=ExperienceLevel.objects.all())


@login_required
def change_level(request):
	try:
		level = UserExperienceLevel.objects.get(user__id=request.user.id)
		initial = {'experience_level': level}
	except UserExperienceLevel.DoesNotExist:
		level = None
		initial = {}

	if request.method == 'POST':
		form = ExperienceForm(request.POST, initial=initial)

		if form.is_valid():
			if level:
				level.experience_level = form.cleaned_data['experience_level']
			else:
				level = UserExperienceLevel(experience_level=form.cleaned_data['experience_level'], user=request.user)

			level.save()

			request.user.message_set.create(message='Successfully set experience level to %s.  It may take up to 10 minutes for this change to appear on /r/homebrewing' % level.experience_level)

			return HttpResponseRedirect('/profile/')
	else:
		form = ExperienceForm(initial=initial)
		
	return render_to_response('homebrewit_experience.html', {'form': form},
			context_instance=RequestContext(request))


# XXX @cache_page(600)
def experience_styles(request):
	return render_to_response('experience_styles.css',
			{'experience_levels': UserExperienceLevel.objects.all()},
			mimetype='text/css')
