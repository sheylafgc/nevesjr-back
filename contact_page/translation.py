from modeltranslation.translator import translator, TranslationOptions
from .models import ContactPage

class ContactPageTranslationOptions(TranslationOptions):
    fields = ('section1_title', 'section1_description', 'section2_title')

translator.register(ContactPage, ContactPageTranslationOptions)
