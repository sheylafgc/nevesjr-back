from django import forms
from .models import BeAPartnerPage

class BeAPartnerPageForm(forms.ModelForm):
    class Meta:
        model = BeAPartnerPage
        fields = '__all__'