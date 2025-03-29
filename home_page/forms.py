from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import HomePage, HomePageDifferentials

class HomePageDifferentialsForm(forms.ModelForm):
    class Meta:
        model = HomePageDifferentials
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget()
        }

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = '__all__'
        widgets = {
            'section3_title': SummernoteWidget(),
            'section4_description': SummernoteWidget(),
            'section5_subtitle': SummernoteWidget(),
            'section6_subtitle': SummernoteWidget(),
        }