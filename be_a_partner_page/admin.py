from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from modeltranslation.utils import get_translation_fields

from .models import BeAPartnerPage
from .forms import BeAPartnerPageForm


class BeAPartnerPageAdmin(SummernoteModelAdmin):
    form = BeAPartnerPageForm
    
    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'section1_banner_description', 
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(BeAPartnerPage, field))

        return translated_fields

    def get_excluded_fields(self):
        summernote_fields = [
            'section1_banner_title', 
            'section1_banner_description', 
            'section1_form_title', 
            'section1_form_description',
        ]
        return summernote_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        self.exclude = self.get_excluded_fields()
        return super().get_form(request, obj, **kwargs)

admin.site.register(BeAPartnerPage, BeAPartnerPageAdmin)