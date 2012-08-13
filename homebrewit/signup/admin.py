from django.contrib import admin
from homebrewit.signup.models import *

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username']

admin.site.register(UserProfile, UserProfileAdmin)
