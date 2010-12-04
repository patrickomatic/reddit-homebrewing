from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render_to_response


def profile(request, username=None):
	if username:
		user = User.objects.get(username=username)
	elif request.user.is_authenticated():
		user = request.user
	else:
		raise Http404

	return render_to_response('homebrewit_profile.html', {'user': user})
