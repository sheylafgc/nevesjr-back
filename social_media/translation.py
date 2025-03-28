from modeltranslation.translator import translator, TranslationOptions
from .models import SocialMedia


class SocialMediaTranslationOptions(TranslationOptions):
    fields = ('label',)

translator.register(SocialMedia, SocialMediaTranslationOptions)
