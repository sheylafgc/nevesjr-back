from django import forms
from .models import OurService


class OurServiceForm(forms.ModelForm):
    class Meta:
        model = OurService
        fields = '__all__'