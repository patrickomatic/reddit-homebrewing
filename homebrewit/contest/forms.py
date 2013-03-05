from django.forms import Form, ModelForm, ModelChoiceField
from contest.models import BJCPJudgingResult, Entry


class JudgingForm(ModelForm):
    class Meta:
        model = BJCPJudgingResult

class JudgeEntrySelectionForm(Form):
        entry = ModelChoiceField(queryset = Entry.objects.all())
