from modeltranslation.translator import translator, TranslationOptions
from .models import FrequentlyQuestions


class FrequentlyQuestionsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)

translator.register(FrequentlyQuestions, FrequentlyQuestionsTranslationOptions)
