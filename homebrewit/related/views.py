from django.shortcuts import render
from homebrewit.related.models import *

def related_subreddits(request):
    return render(request, 'related/related_subreddits.html', 
            {'related_subreddits': RelatedSubreddit.objects.values('display', 'url')})
