from decimal import Decimal, ROUND_DOWN
from django.db import models

from vehicles.models import Vehicle

from .choices import *


class Booking(models.Model):
    from_route = models.CharField(max_length=255, blank=True, null=True)
    to_route = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.TimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    estimated_time = models.TimeField(blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)

    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    booking_for = models.CharField(max_length=20, choices=BOOKING_FOR_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_intent_id = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=255, blank=True, null=True)
    payment_brand = models.CharField(max_length=255, blank=True, null=True)

    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.first_name} {self.last_name} on {self.date} at {self.hour}"
