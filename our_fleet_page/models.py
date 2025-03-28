from django.db import models
from django.core.exceptions import ValidationError

from vehicles.models import Vehicle


class OurFleetPage(models.Model):
    section1_title = models.CharField(max_length=255, blank=True, null=True)
    section1_subtitle = models.CharField(max_length=255, blank=True, null=True)
    section1_banner = models.ImageField(upload_to='our_fleet_page/section1/banner', blank=True, null=True)
    section2_vehicles = models.ManyToManyField(Vehicle, related_name='our_fleet_pages', blank=True, null=True)

    def save(self, *args, **kwargs):
        if OurFleetPage.objects.exists() and not self.pk:
            raise ValidationError("Only one OurFleetPage registration is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Our Fleet Page"