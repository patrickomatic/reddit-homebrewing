from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext

from homebrewit.contest.models import *


# XXX don't allow for setting the user here
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry


def register(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			request.user.message_set.create(message='You are now entered in the %s category' % form.cleaned_data['style'])
	else:
		form = EntryForm()

	return render_to_response('homebrewit_contest_register.html', {'form': form},
		context_instance=RequestContext(request))
