from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^contest/', include('homebrewit.contest.urls')),
    (r'^profile/', include('homebrewit.profile.urls')),
    (r'^experience/', include('homebrewit.experiencelevel.urls')),
    (r'^admin/', include(admin.site.urls)),

    ('', include('homebrewit.signup.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
			(r'^media/(?P<path>.*)$', 'django.views.static.serve',
				{'document_root': settings.MEDIA_ROOT})
	)

