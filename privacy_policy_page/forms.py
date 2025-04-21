from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import PrivacyPolicyPage


class PrivacyPolicyPageForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicyPage
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }