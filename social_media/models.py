from django.db import models
from django.core.exceptions import ValidationError


class SocialMedia(models.Model):
    phone_whatsapp1 = models.CharField(max_length=30, blank=True, null=True)
    phone_whatsapp2 = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=30, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    x = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        if SocialMedia.objects.exists() and not self.pk:
            raise ValidationError("Only one SocialMedia registration is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Social Media"