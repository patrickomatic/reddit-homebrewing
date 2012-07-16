from django.contrib import admin
from homebrewit.related.models import *

class RelatedSubredditAdmin(admin.ModelAdmin):
	search_fields = ['display', 'url']


admin.site.register(RelatedSubreddit, RelatedSubredditAdmin)
