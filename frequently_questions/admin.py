from django.contrib import admin
from .models import FrequentlyQuestions
from .forms import FrequentlyQuestionsForm


class FrequentlyQuestionsAdmin(admin.ModelAdmin):
    form = FrequentlyQuestionsForm
    exclude = ['question', 'answer',]

admin.site.register(FrequentlyQuestions, FrequentlyQuestionsAdmin)