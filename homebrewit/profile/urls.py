from django.conf.urls import patterns, url
from django.contrib import admin

from homebrewit.profile import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'edit$', 'edit_profile'),
    (r'password$', 'change_password'),
    url(r'^(?P<username>[\w_-]+)|$', views.ProfileView.as_view(), name='profile'),
)
