from django import forms
from .models import OurFleetPage


class OurFleetPageForm(forms.ModelForm):
    class Meta:
        model = OurFleetPage
        fields = '__all__'