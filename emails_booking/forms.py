from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import EmailRaceHiring, EmailRaceFinish


class EmailRaceHiringForm(forms.ModelForm):
    class Meta:
        model = EmailRaceHiring
        fields = '__all__'
        widgets = {
            'message': SummernoteWidget(),
        }

class EmailRaceFinishForm(forms.ModelForm):
    class Meta:
        model = EmailRaceFinish
        fields = '__all__'
        widgets = {
            'message': SummernoteWidget(),
        }