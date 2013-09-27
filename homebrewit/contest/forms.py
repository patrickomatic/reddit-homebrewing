from django.forms import Form, ModelForm, ModelChoiceField, CharField, HiddenInput, Textarea
from homebrewit.contest.models import BeerStyle, BJCPJudgingResult, Entry, ContestYear
from django.contrib.auth.models import User
import datetime


class JudgingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(JudgingForm, self).__init__(*args, **kwargs)
        

    class Meta:
        model = BJCPJudgingResult
        exclude = ('judge',)
        widgets = {
                    'aroma_description': Textarea,
                    'appearance_description': Textarea,
                    'flavor_description': Textarea,
                    'mouthfeel_description': Textarea,
                    'overall_impression_description': Textarea,
                    }
        
        
class JudgeEntrySelectionForm(Form):
    def __init__(self, *args, **kwargs):
        self.thisyear = ContestYear.objects.get(contest_year = datetime.datetime.now().year)
        self.user = kwargs.pop('user', None)
        super(JudgeEntrySelectionForm, self).__init__(*args, **kwargs)
        self.fields['entry'] = ModelChoiceField(
                                                queryset = Entry.objects 
                                                    .filter(style__in = BeerStyle.objects 
                                                    .filter(judge = self.user, contest_year = self.thisyear)) 
                                                    .filter(bjcp_judging_result = None))
