from modeltranslation.translator import translator, TranslationOptions
from .models import Vehicle, OurFleetPage


class VehicleTranslationOptions(TranslationOptions):
    fields = ('car_name', 'car_type', 'car_overview', 'car_amenities', 'car_best_for_services',)

class OurFleetPageTranslationOptions(TranslationOptions):
    fields = ('section1_title', 'section1_subtitle',) 

translator.register(Vehicle, VehicleTranslationOptions)
translator.register(OurFleetPage, OurFleetPageTranslationOptions)
