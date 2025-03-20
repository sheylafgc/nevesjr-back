from django import forms
from .models import ContactPage

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = '__all__'