from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from modeltranslation.utils import get_translation_fields

from .models import Vehicle
from .forms import VehicleForm


class VehicleAdmin(SummernoteModelAdmin):
    form = VehicleForm

    def get_summernote_fields(self, request, obj=None):
        summernote_fields = [
            'car_overview',
            'car_amenities',
            'car_best_for_services',
        ]
        
        translated_fields = []
        for field in summernote_fields:
            translated_fields.extend(get_translation_fields(Vehicle, field))

        return translated_fields

    def get_excluded_fields(self):
        summernote_fields = [
            'car_name', 
            'car_type', 
            'car_overview',
            'car_amenities',
            'car_best_for_services',
        ]
        return summernote_fields

    def get_form(self, request, obj=None, **kwargs):
        self.summernote_fields = self.get_summernote_fields(request, obj)
        self.exclude = self.get_excluded_fields()
        return super().get_form(request, obj, **kwargs)

admin.site.register(Vehicle, VehicleAdmin)