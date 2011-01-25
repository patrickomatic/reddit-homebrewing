import datetime

from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from homebrewit.contest.models import *


class EntryForm(forms.Form):
	beer_name = forms.CharField(max_length=255, required=False)
	style = forms.ModelChoiceField(queryset=BeerStyle.objects.filter(contest_year__contest_year=datetime.datetime.now().year))
	special_ingredients = forms.CharField(max_length=1000, required=False)

@login_required
def register(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			entry = Entry(style=form.cleaned_data['style'], 
					beer_name=form.cleaned_data['beer_name'], 
					special_ingredients=form.cleaned_data['special_ingredients'],
					user=request.user)
			entry.save()

			request.user.message_set.create(message='You are now entered in the %s category' % entry.style)
	else:
		form = EntryForm()

	return render_to_response('homebrewit_contest_register.html', {'form': form},
		context_instance=RequestContext(request))


def style(request, year, style_id):
	try:
		style = BeerStyle.objects.get(pk=style_id)
		assert style.contest_year.contest_year == int(year)
	except BeerStyle.DoesNotExist:
		raise Http404

	entries = Entry.objects.filter(style=style)

	return render_to_response('homebrewit_contest_style.html',
			{'style': style, 'entries': entries}, 
			context_instance=RequestContext(request))


def contest_year(request, year):
	styles = {}
	for style in BeerStyle.objects.filter(contest_year__contest_year=year):
		top_11 = Entry.objects.get_top_n(style, 11)
		styles[style] = {
			'entries': top_11[:10],
			'has_more': len(top_11) > 10,
		}


	return render_to_response('homebrewit_contest_year.html', 
			{'styles': styles, 'year': int(year)},
			context_instance=RequestContext(request))


def entry(request, year, style_id, entry_id):
	try:
		entry = Entry.objects.get(pk=entry_id)
		assert entry.style.id == int(style_id)
		assert entry.style.contest_year.contest_year == int(year)
	except Entry.DoesNotExist:
		raise Http404

	return render_to_response('homebrewit_contest_entry.html',
			{'entry': entry, 'judging_results': JudgingResult.objects.filter(entry=entry)}, 
			context_instance=RequestContext(request))


# XXX @cache_page(600)
def winner_styles(request):
	return render_to_response('winner_styles.css', 
			{'icon_url': settings.WINNER_ICON, 'winners': Entry.objects.get_all_winners()},
			mimetype='text/css')
