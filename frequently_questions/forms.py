from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import FrequentlyQuestions


class FrequentlyQuestionsForm(forms.ModelForm):
    class Meta:
        model = FrequentlyQuestions
        fields = '__all__'
        widgets = {
            'question': SummernoteWidget(),
            'answer': SummernoteWidget(),
        }