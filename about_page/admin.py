from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from modeltranslation.utils import get_translation_fields

from .models import AboutPage, TeamMember
from .forms import AboutPageForm, TeamMemberForm


class AboutPageAdmin(SummernoteModelAdmin):
    form = AboutPageForm

    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'section1_subtitle', 
            'section2_description', 
            'section3_description', 
            'section4_description', 
            'section5_description'
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(AboutPage, field))

        return translated_fields

    def get_excluded_fields(self):
        summernote_fields = [
            'section1_title', 
            'section1_subtitle', 
            'section2_title', 
            'section2_description', 
            'section3_title', 
            'section3_description',
            'section4_title', 
            'section4_description', 
            'section5_title', 
            'section5_description',
            'section6_title', 
        ]
        return summernote_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        self.exclude = self.get_excluded_fields()
        return super().get_form(request, obj, **kwargs)
    
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberForm
    exclude = ['role',]

admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)