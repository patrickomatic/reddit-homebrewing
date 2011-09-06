from django import forms
from django.contrib import admin
from django.db import models

from homebrewit.contest.models import *


class JudgingResultAdminForm(forms.ModelForm):
	class Meta:
		model = JudgingResult
		widgets = {
				'aroma_description': forms.Textarea(),
				'appearance_description': forms.Textarea(),
				'mouthfeel_description': forms.Textarea(),
				'flavor_description': forms.Textarea(),
				'overall_impression_description': forms.Textarea(),
		}

class JudgingResultAdmin(admin.ModelAdmin):
	form = JudgingResultAdminForm

admin.site.register(BeerStyle)
admin.site.register(ContestYear)
admin.site.register(Entry)
admin.site.register(JudgingResult, JudgingResultAdmin)
