from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import OurService


class OurServiceForm(forms.ModelForm):
    class Meta:
        model = OurService
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }