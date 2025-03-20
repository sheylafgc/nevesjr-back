from modeltranslation.translator import translator, TranslationOptions
from .models import ContactPage

class ContactPageTranslationOptions(TranslationOptions):
    fields = ('section1_form_title', 'section1_form_description', 'section2_banner_title')

translator.register(ContactPage, ContactPageTranslationOptions)
