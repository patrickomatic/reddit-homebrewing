from django import forms
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

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


def winners(request, year):
	entries = Entry.objects.filter(winner=True, year=year)
	return render_to_response('homebrewit_contest_winners.html', 
			{'entries': entries, 'year': year},
			context_instance=RequestContext(request))


def entry(request, year, entry_id):
	try:
		entry = Entry.objects.get(id=entry_id, year=year)
	except Entry.DoesNotExist:
		raise Http404

	return render_to_response('homebrewit_contest_entry.html',
			{'year': year, 'entry': entry},
			context_instance=RequestContext(request))
