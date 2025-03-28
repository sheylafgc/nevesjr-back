from django.db.models.signals import post_save
from django.dispatch import receiver

from our_services.models import OurService 

from .models import OurServicesPage


@receiver(post_save, sender=OurService)
def create_our_service_page(sender, instance, created, **kwargs):
    if created:
        our_service_page, _ = OurServicesPage.objects.get_or_create() 
        our_service_page.section2_services.add(instance)
