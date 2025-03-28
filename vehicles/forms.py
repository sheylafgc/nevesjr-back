from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'car_overview': SummernoteWidget(),
            'car_amenities': SummernoteWidget(),
            'car_best_for_services': SummernoteWidget(),
        }