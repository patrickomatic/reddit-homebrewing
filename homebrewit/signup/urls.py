from django.conf import settings
from django.conf.urls import patterns
from django.contrib import admin

admin.autodiscover()

    
urlpatterns = patterns('homebrewit.signup.views',
    (r'^logout', 'logout'),
    (r'^signup', 'signup'),
    (r'^$', 'index'),
)

