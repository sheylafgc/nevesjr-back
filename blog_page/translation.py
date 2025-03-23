from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'category')

translator.register(Blog, BlogTranslationOptions)
