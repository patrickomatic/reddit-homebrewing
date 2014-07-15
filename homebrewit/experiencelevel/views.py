import datetime, json, urllib2

from django import forms
from django.core.mail import mail_admins
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from homebrewit.experiencelevel.models import *
from homebrewit.reddit import set_flair, reddit_login, RedditRateLimitingError


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

                message = 'Successfully set experience level to %s.' % level.experience_level
                success = True
            except urllib2.HTTPError:
                message = 'Whoops! There was an error setting your experience level.  This usually happens when reddit\'s API is down.  Try again later and if you continue to have problems, please contact the moderators.'
                success = False
            except RedditRateLimitingError:
                message = 'Whoops! There was an error setting your experience level.  It appears that reddit\'s servers are not accepting requests at the moment.  Please try again in a couple of minutes.'
                success = False

            if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                return HttpResponse(json.dumps({'success': success, 'message': message}), content_type='application/json')
            else:
                messages.success(request, message)
                if success:
                    return HttpResponseRedirect('/profile/')
    else:
        form = ExperienceForm(initial=initial)
        
    return render(request, 'experiencelevel/edit.html', {
                'current_level': level,
                'experience_levels': ExperienceLevel.objects.all(),
                'form': form,
            })
