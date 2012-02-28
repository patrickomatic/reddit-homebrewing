import datetime

from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson as json
from django.views.decorators.cache import cache_page

from homebrewit.contest.models import *
from homebrewit.signup.models import UserProfile



@login_required
def register(request):
	contest_year = ContestYear.objects.get_current_contest_year()
	styles = BeerStyle.objects.filter(contest_year=contest_year)
	style_subcategories = BeerStyleSubcategory.objects.filter(beer_style__contest_year=contest_year).order_by('name')

	# this class definition is inside of this function because it needs
	# to access local variables
	class EntryForm(forms.Form):
		style = forms.ModelChoiceField(queryset=styles)
		style_subcategory = forms.ModelChoiceField(queryset=style_subcategories, required=False)
		beer_name = forms.CharField(max_length=255, required=False)
		special_ingredients = forms.CharField(max_length=1000, required=False)

		def __init__(self, *args, **kwargs):
			self.request = kwargs.pop('request', None)
			super(EntryForm, self).__init__(*args, **kwargs)


		def clean_style_subcategory(self):
			cd = self.cleaned_data
			style = cd['style']

			if not style.has_subcategories():
				return None
			
			if not cd.get('style_subcategory'):
				raise forms.ValidationError("You must specify a subcategory.")
			subcategory = cd['style_subcategory']
			if subcategory.beer_style != style:
				raise forms.ValidationError("That subcategory doesn't belong to this style")
			
			return subcategory


		def clean(self):
			try:
				Entry.objects.get(style=self.cleaned_data['style'], user=self.request.user)
				raise forms.ValidationError('You have already entered in this category')
			except Entry.DoesNotExist:
				return self.cleaned_data


	# they can't register for the contest unless their profile is complete
	try:
		request.user.get_profile()
	except UserProfile.DoesNotExist:
		request.user.message_set.create(message='You must set your address before you can enter the homebrew contest.')
		return HttpResponseRedirect('/profile/edit?next=/contest/register')

	contest_year = ContestYear.objects.get_current_contest_year()
	if not contest_year.allowing_entries:
		raise Http404

	if request.method == 'POST':
		form = EntryForm(request.POST, request=request)
		if form.is_valid():
			entry = Entry(style=form.cleaned_data['style'], 
					beer_name=form.cleaned_data['beer_name'], 
					special_ingredients=form.cleaned_data['special_ingredients'],
					user=request.user)

			if 'style_subcategory' in form.cleaned_data:
				entry.style_subcategory = form.cleaned_data['style_subcategory']

			entry.save()

			entry.send_shipping_email()

			request.user.message_set.create(message='You are now entered in the %s category' % entry.style)
	else:
		form = EntryForm()


	# make some json-friendly style data
	style_data = dict([(style.id, []) for style in styles])
	for sub in style_subcategories:
		style_data[sub.beer_style.id].append({'id': sub.id, 'name': sub.name})

	return render_to_response('homebrewit_contest_register.html', {
			'form': form,
			'style_data_as_json': json.dumps(style_data),
		}, context_instance=RequestContext(request))


def style(request, year, style_id):
	try:
		style = BeerStyle.objects.get(pk=style_id)
		assert style.contest_year.contest_year == int(year)
	except BeerStyle.DoesNotExist:
		raise Http404

	scored_entries = list(Entry.objects.filter(style=style, score__isnull=False).order_by('-score'))

	scored_entries.extend(Entry.objects.filter(style=style, score__isnull=True))
	
	address = None
	if style.judge:
		address = style.judge.get_profile()

	return render_to_response('homebrewit_contest_style.html', {
			'style': style, 
			'entries': scored_entries,
			'address': address,
		}, context_instance=RequestContext(request))


def contest_year(request, year):
	contest_year = ContestYear.objects.get(contest_year=year)

	styles = {}
	for style in BeerStyle.objects.filter(contest_year=contest_year):
		top_31 = Entry.objects.filter(style=style)[:31]
		styles[style] = {
			'entries': top_31[:30],
			'has_more': len(top_31) > 30,
		}


	return render_to_response('homebrewit_contest_year.html', {
				'styles': styles, 
				'year': int(year),
				'contest_year': contest_year,
			}, context_instance=RequestContext(request))


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
