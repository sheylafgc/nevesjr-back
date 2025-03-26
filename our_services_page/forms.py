from django import forms
from .models import OurServicesPage

class OurServicesPageForm(forms.ModelForm):
    class Meta:
        model = OurServicesPage
        fields = '__all__'