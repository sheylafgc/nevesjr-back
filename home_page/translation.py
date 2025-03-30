from modeltranslation.translator import translator, TranslationOptions
from .models import HomePage, HomePageDifferentials


class HomePageTranslationOptions(TranslationOptions):
    fields = (
        'section1_title', 
        'section2_title',
        'section2_description',
        'section3_title', 
        'section4_title', 
        'section4_description', 
        'section5_title', 
        'section5_subtitle', 
        'section6_title', 
        'section6_subtitle', 
        'section7_title', 
        'section8_title',
    )

class HomePageDifferentialsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(HomePage, HomePageTranslationOptions)
translator.register(HomePageDifferentials, HomePageDifferentialsTranslationOptions)
