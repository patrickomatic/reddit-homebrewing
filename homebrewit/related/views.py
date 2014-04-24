from django.shortcuts import render
from homebrewit.related.models import *

def view_related(request):
	return render(request, 'homebrewit_related_reddits.html', 
			{'related_subreddits': RelatedSubreddit.objects.values('display', 'url')})
