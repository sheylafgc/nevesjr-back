from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from modeltranslation.utils import get_translation_fields

from .models import HomePage, HomePageDifferentials
from .forms import HomePageForm, HomePageDifferentialsForm


class HomePageAdmin(SummernoteModelAdmin):
    form = HomePageForm

    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'section3_title', 
            'section4_description', 
            'section5_subtitle', 
            'section6_subtitle',
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(HomePage, field))

        return translated_fields

    def get_excluded_fields(self):
        summernote_fields = [
            'section1_title', 
            'section2_title', 
            'section3_title', 
            'section4_title', 
            'section4_description', 
            'section5_title', 
            'section5_subtitle', 
            'section6_title', 
            'section6_subtitle', 
            'section7_title', 
            'section8_title',
        ]
        return summernote_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        self.exclude = self.get_excluded_fields()
        return super().get_form(request, obj, **kwargs)
    
class HomePageDifferentialsAdmin(SummernoteModelAdmin):
    form = HomePageDifferentialsForm
    exclude = ['title', 'description',]

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(HomePageDifferentials, HomePageDifferentialsAdmin)