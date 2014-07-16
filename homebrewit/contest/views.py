import datetime, json, logging

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from rest_framework import generics, status
from rest_framework.response import Response

from .forms import JudgeEntrySelectionForm, JudgingForm
from .models import *
from .serializers import *
from homebrewit.signup.models import UserProfile


logger = logging.getLogger(__name__)


class BeerStyleListView(generics.ListAPIView):
    serializer_class = BeerStyleSerializer
    model = BeerStyle

    def get_queryset(self):
        return BeerStyle.objects.for_year(self.kwargs['year'])


class EntriesListView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    model = Entry

    def get_queryset(self):
        Entry.objects.filter(contest_year__contest_year=self.kwargs['contest_year'])

    def get_object(self):
        Entry.get(pk=self.kwargs['entry_id'])

    def pre_save(self, entry):
        entry.user_id = self.request.user.id

    def post_save(self, entry, created):
        if created: 
            ContestYear.objects.expire_get_all_year_summary_cache()
            entry.send_shipping_email()



@login_required
def register(request, year):
    contest_year = ContestYear.objects.get_current_contest_year()

    if not contest_year or contest_year.contest_year != int(year):
        raise Http404

    styles = contest_year.beer_styles

    try:
        request.user.get_profile()
    except UserProfile.DoesNotExist:
        messages.error(request, 'You must set your address before you can enter the homebrew contest.')
        # XXX can we use url helpers here
        return HttpResponseRedirect('/profile/edit?next=/contests/%s/register' % contest_year.contest_year)

    return render(request, 'contest/register.html', {'contest_year': contest_year})


def style(request, year, style_id):
    try:
        style = BeerStyle.objects.get(pk=style_id)
        assert style.contest_year.contest_year == int(year)
    except BeerStyle.DoesNotExist:
        raise Http404
    
    address = None
    if style.judge:
        try:
            address = style.judge.get_profile()
        except UserProfile.DoesNotExist:
            pass

    return render(request, 'contest/style.html', {
        'style': style, 
        'entries': Entry.objects.for_beer_style(style),
        'address': address
    })


def contest_year(request, year):
    contest_year = ContestYear.objects.get(contest_year=year)

    styles = {}
    for style in BeerStyle.objects.top_level_styles_for_year(contest_year.contest_year):
        top_31 = Entry.objects.filter(style=style)[:31]
        styles[style] = {
            'entries': top_31[:30],
            'has_more': len(top_31) > 30,
        }


    return render(request, 'contest/contest_year.html', {
                'styles': styles, 
                'year': int(year),
                'contest_year': contest_year})


class BJCPJudgingResultForm(ModelForm):
    class Meta:
        model = BJCPJudgingResult

def entry(request, year, style_id, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
        assert entry.style.contest_year.contest_year == int(year)
    except Entry.DoesNotExist:
        raise Http404


    # this split is an unfortunate artifact of switching the way that we judge the contest
    # after already having data.  basically, if it uses the new BJCP scoresheet, we show
    # that template, otherwise the other (old) one
    if entry.bjcp_judging_result:
        return render(request, 'contest/bjcp_entry.html', {
                'entry': entry,
                'form': BJCPJudgingResultForm(instance=entry.bjcp_judging_result)})
    else:
        return render(request, 'contest/entry.html', {
                'entry': entry,
                'judging_results': JudgingResult.objects.filter(entry=entry)})



@login_required
def entry_judging_form(request):
    if not BeerStyle.objects.filter(judge = request.user.id):
        raise RuntimeError(request.user.username + " is not a judge.")

    if request.method == 'POST':
        try:
            this_entry = Entry.objects.get(pk = request.POST['entry'])
        except ValueError:
            raise RuntimeError("Select an entry to judge!")
        judgable_categories = BeerStyle.objects.filter(judge = request.user)
        if not this_entry.style in judgable_categories:
            raise RuntimeError(request.user.username + " is not a valid judge for category: " + this_entry.style.name)
        if this_entry.user == request.user:
            raise RuntimeError(request.user.username + " is not allowed to judge his own entry.")

        entry_selection_form = JudgeEntrySelectionForm(user = request.user)
        judge_form = JudgingForm(request.POST)

        if judge_form.is_valid():
            judge_result = judge_form.save(commit = False)
            judge_result.judge = request.user
            judge_result.save()

            this_entry.bjcp_judging_result = judge_result
            this_entry.score = judge_result.overall_rating()
            this_entry.save()

            judge_form = JudgingForm()

            return render(request, 'contest/judging_form.html', {
                            'entry_selection_form': entry_selection_form, 
                            'judge_form': judge_form, 
                            'status_message': 'Judging for: ' + this_entry.beer_name + ' complete!'})
    else:
        entry_selection_form = JudgeEntrySelectionForm(user = request.user)
        judge_form = JudgingForm()

    return render(request, 'contest/judging_form.html', {
            'entry_selection_form': entry_selection_form, 
            'judge_form': judge_form, 
            'status_message': None})
