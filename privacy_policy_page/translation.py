from modeltranslation.translator import translator, TranslationOptions
from .models import PrivacyPolicyPage


class PrivacyPolicyPageTranslationOptions(TranslationOptions):
    fields = ('content',)

translator.register(PrivacyPolicyPage, PrivacyPolicyPageTranslationOptions)