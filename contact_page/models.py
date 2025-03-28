from django.db import models
from django.core.exceptions import ValidationError

from social_media.models import SocialMedia


class ContactPage(models.Model):
    section1_banner = models.ImageField(upload_to='contact_page/section1/banner', blank=True, null=True)
    section1_form_title = models.CharField(max_length=255, blank=True, null=True)
    section1_form_description = models.CharField(max_length=255, blank=True, null=True)
    section1_social_media = models.OneToOneField(SocialMedia, on_delete=models.CASCADE, null=True, blank=True)
    section2_banner = models.ImageField(upload_to='contact_page/section2/banner', blank=True, null=True)
    section2_banner_title = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if ContactPage.objects.exists() and not self.pk:
            raise ValidationError('Only one ContactPage registration is allowed.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Contact Page'