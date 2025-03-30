from django import forms
from .models import FrequentlyQuestions


class FrequentlyQuestionsForm(forms.ModelForm):
    class Meta:
        model = FrequentlyQuestions
        fields = '__all__'