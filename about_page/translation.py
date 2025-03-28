from modeltranslation.translator import translator, TranslationOptions
from .models import AboutPage, TeamMember


class AboutPageTranslationOptions(TranslationOptions):
    fields = (
        'section1_title', 
        'section1_subtitle', 
        'section2_title', 
        'section2_description', 
        'section3_title', 
        'section3_description', 
        'section4_title', 
        'section4_description', 
        'section5_title', 
        'section5_description', 
        'section6_title',
    )

class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('role',)

translator.register(AboutPage, AboutPageTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)
