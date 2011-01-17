import datetime

from django import forms
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from homebrewit.contest.models import *


class EntryForm(forms.Form):
	style = forms.ModelChoiceField(queryset=BeerStyle.objects.all())

@login_required
def register(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			entry = Entry(style=form.cleaned_data['style'], user=request.user)
			entry.save()

			request.user.message_set.create(message='You are now entered in the %s category' % entry.style)
	else:
		form = EntryForm()

	return render_to_response('homebrewit_contest_register.html', {'form': form},
		context_instance=RequestContext(request))


def styles(request):
	styles = BeerStyle.objects.all()
	return render_to_response('homebrewit_contest_styles.html', {'styles': styles},
			context_instance=RequestContext(request))


def contest_year(request, year):
	entries = Entry.objects.filter(style__contest_year=year)
	return render_to_response('homebrewit_contest_year.html', 
			{'entries': entries, 'year': year},
			context_instance=RequestContext(request))


def entry(request, year, entry_id):
	try:
		entry = Entry.objects.get(id=entry_id, contest_year=year)
	except Entry.DoesNotExist:
		raise Http404

	return render_to_response('homebrewit_contest_entry.html',
			{'year': year, 'entry': entry},
			context_instance=RequestContext(request))


@cache_page(60 * 10)
def winner_styles(request):
	resp = HttpResponse("\n".join(["""
a[href*="user/%(username)s":after {
	content: url(%(icon_url)s);
}
	""" % {
			'username': winner.username,
			'icon_url': settings.WINNER_ICON,
		} for winner in Entry.objects.get_all_winners()]), mimetype='text/css')

	resp['Content-Type'] = 'text/css'
	return resp
