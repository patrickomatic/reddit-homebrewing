from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, patterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    (r'^contest/', include('homebrewit.contest.urls')),
    (r'^profile/', include('homebrewit.profile.urls')),
    (r'^experience/', include('homebrewit.experiencelevel.urls')),
    (r'^related/', include('homebrewit.related.urls')),
    (r'^admin/', include(admin.site.urls)),
    ('', include('homebrewit.signup.urls')),
) + static(settings.STATIC_URL)
