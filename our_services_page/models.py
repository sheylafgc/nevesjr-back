from django.db import models
from django.core.exceptions import ValidationError

from our_services.models import OurService


class OurServicesPage(models.Model):
    section1_title = models.TextField(blank=True, null=True)
    section1_subtitle = models.TextField(blank=True, null=True)
    section1_image = models.ImageField(upload_to='our_service_page/section1/image', blank=True, null=True)
    section2_services = models.ManyToManyField(OurService, related_name='our_services_pages', blank=True, null=True)
    section3_title = models.TextField(blank=True, null=True)
    section3_banner = models.ImageField(upload_to='our_service_page/section3/banner', blank=True, null=True)

    def save(self, *args, **kwargs):
        if OurServicesPage.objects.exists() and not self.pk:
            raise ValidationError('Only one OurServicePage registration is allowed.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Our Services Page'