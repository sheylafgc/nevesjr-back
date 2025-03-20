from modeltranslation.translator import translator, TranslationOptions
from .models import BeAPartnerPage

class BeAPartnerPageTranslationOptions(TranslationOptions):
    fields = ('section1_banner_title', 'section1_banner_description', 'section1_form_title', 'section1_form_description')

translator.register(BeAPartnerPage, BeAPartnerPageTranslationOptions)