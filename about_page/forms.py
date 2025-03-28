from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import AboutPage, TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = '__all__'
        widgets = {
            'section1_subtitle': SummernoteWidget(),
            'section2_description': SummernoteWidget(),
            'section3_description': SummernoteWidget(),
            'section4_description': SummernoteWidget(),
            'section5_description': SummernoteWidget(),
        }