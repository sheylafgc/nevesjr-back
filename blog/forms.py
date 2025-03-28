from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }