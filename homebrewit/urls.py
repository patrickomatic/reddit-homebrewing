from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, patterns
from django.conf.urls.static import static

print "In urls?"
admin.autodiscover()

urlpatterns = patterns('',
    (r'^contest/', include('homebrewit.contest.urls')),
    (r'^profile/', include('homebrewit.profile.urls')),
    (r'^experience/', include('homebrewit.experiencelevel.urls')),
    (r'^related/', include('homebrewit.related.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ('', include('homebrewit.signup.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#	urlpatterns += patterns('',
#			(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#				{'document_root': settings.MEDIA_ROOT})
#	)

