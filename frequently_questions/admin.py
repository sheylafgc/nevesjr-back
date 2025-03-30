from django.contrib import admin

from modeltranslation.utils import get_translation_fields

from .models import FrequentlyQuestions
from .forms import FrequentlyQuestionsForm


class FrequentlyQuestionsAdmin(admin.ModelAdmin):
    form = FrequentlyQuestionsForm
    # exclude = ['question', 'answer',]
    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'question', 
            'answer', 
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(FrequentlyQuestions, field))

        return translated_fields

    def get_excluded_fields(self):
        summernote_fields = [
            'question', 
            'answer',
        ]
        return summernote_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        self.exclude = self.get_excluded_fields()
        return super().get_form(request, obj, **kwargs)

admin.site.register(FrequentlyQuestions, FrequentlyQuestionsAdmin)