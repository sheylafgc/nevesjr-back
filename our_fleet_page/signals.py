from django.db.models.signals import post_save
from django.dispatch import receiver

from vehicles.models import Vehicle

from .models import OurFleetPage


@receiver(post_save, sender=Vehicle)
def create_our_fleet_page(sender, instance, created, **kwargs):
    if created:
        our_fleet_page, _ = OurFleetPage.objects.get_or_create() 
        our_fleet_page.section2_vehicles.add(instance)