from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static

from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()

urlpatterns = patterns('',
    (r'^contests/', include('homebrewit.contest.urls')),
    (r'^profile/', include('homebrewit.profile.urls')),
    (r'^experience/', include('homebrewit.experiencelevel.urls')),
    (r'^related/', include('homebrewit.related.urls')),
    (r'^admin/', include(admin.site.urls)),
    ('', include('homebrewit.signup.urls')),
    url(r'^', include(router.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
