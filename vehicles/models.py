from django.db import models


class Vehicle(models.Model):
    car_name = models.CharField(max_length=255, blank=True, null=True)
    car_type = models.CharField(max_length=255, blank=True, null=True)
    quantity_seats = models.IntegerField(blank=True, null=True)
    quantity_luggage = models.IntegerField(blank=True, null=True)
    car_image = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    price_km = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_hour = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    car_overview = models.TextField(blank=True, null=True)
    car_amenities = models.TextField(blank=True, null=True)
    car_best_for_services = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.car_name