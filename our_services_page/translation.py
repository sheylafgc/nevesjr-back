from modeltranslation.translator import translator, TranslationOptions
from .models import OurService, OurServicesPage


class OurServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)

class OurServicesPageTranslationOptions(TranslationOptions):
    fields = ('section1_title', 'section1_subtitle', 'section3_title',) 

translator.register(OurService, OurServiceTranslationOptions)
translator.register(OurServicesPage, OurServicesPageTranslationOptions)
