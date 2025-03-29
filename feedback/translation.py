from modeltranslation.translator import translator, TranslationOptions
from .models import Feedback


class FeedbackTranslationOptions(TranslationOptions):
    fields = ('role', 'opinion',)

translator.register(Feedback, FeedbackTranslationOptions)
