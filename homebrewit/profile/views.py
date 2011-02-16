from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from homebrewit.contest.models import *
from homebrewit.experiencelevel.models import *


# XXX allow for setting your address info
def profile(request, user):
	level_image = None

	try:
		level = UserExperienceLevel.objects.get(user=request.user)
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

