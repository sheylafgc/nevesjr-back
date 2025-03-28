from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import BeAPartnerPage


class BeAPartnerPageForm(forms.ModelForm):
    class Meta:
        model = BeAPartnerPage
        fields = '__all__'
        widgets = {
            'section1_banner_description': SummernoteWidget(),
        }