from django.contrib import admin
from .models import Vehicle
from .forms import VehicleForm


class VehicleAdmin(admin.ModelAdmin):
    form = VehicleForm
    exclude = ['car_name', 'car_type', 'car_overview', 'car_amenities', 'car_best_for_services',]

admin.site.register(Vehicle, VehicleAdmin)