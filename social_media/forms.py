from django import forms
from .models import SocialMedia


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'