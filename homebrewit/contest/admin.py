from django import forms
from django.contrib import admin
from django.db import models

from homebrewit.contest.models import *


class BJCPJudgingResultAdminForm(forms.ModelForm):
    class Meta:
        model = BJCPJudgingResult
        widgets = {
                'aroma_description': forms.Textarea(),
                'appearance_description': forms.Textarea(),
                'mouthfeel_description': forms.Textarea(),
                'flavor_description': forms.Textarea(),
                'overall_impression_description': forms.Textarea(),
        }

class BJCPJudgingResultAdmin(admin.ModelAdmin):
    form = BJCPJudgingResultAdminForm

class ContestYearAdminForm(forms.ModelForm):
    class Meta:
        model = ContestYear
        widgets = { 'prize_description': forms.Textarea(), }

class ContestYearAdmin(admin.ModelAdmin):
    form = ContestYearAdminForm

admin.site.register(BeerDetail)
admin.site.register(BeerDetailChoice)
admin.site.register(BeerStyle)
admin.site.register(BJCPJudgingResult, BJCPJudgingResultAdmin)
admin.site.register(ContestYear, ContestYearAdmin)
admin.site.register(Entry)
admin.site.register(EntryBeerDetail)
admin.site.register(MultipleChoiceBeerDetail)
admin.site.register(TextBeerDetail)
