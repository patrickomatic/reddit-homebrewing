from django.conf.urls.defaults import *

urlpatterns = patterns('homebrewit.related.views',
	(r'^$', 'view_related'),
)
