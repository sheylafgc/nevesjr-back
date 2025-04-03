from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from modeltranslation.utils import get_translation_fields

from .models import EmailRaceHiring, EmailRaceFinish
from .forms import EmailRaceHiringForm, EmailRaceFinishForm


class EmailRaceHiringAdmin(SummernoteModelAdmin):
    form = EmailRaceHiringForm

    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'message',
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(EmailRaceHiring, field))

        return translated_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        return super().get_form(request, obj, **kwargs)
    

class EmailRaceFinishAdmin(admin.ModelAdmin):
    form = EmailRaceFinishForm

    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'message',
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(EmailRaceFinish, field))

        return translated_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        return super().get_form(request, obj, **kwargs)

admin.site.register(EmailRaceHiring, EmailRaceHiringAdmin)
admin.site.register(EmailRaceFinish, EmailRaceFinishAdmin)