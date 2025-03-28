from django.db import models
from django.core.exceptions import ValidationError


class BeAPartnerPage(models.Model):
    section1_banner = models.ImageField(upload_to='be_a_partner_page/section1/banner', blank=True, null=True)
    section1_banner_title = models.CharField(max_length=255, blank=True, null=True)
    section1_banner_description = models.TextField(blank=True, null=True)
    section1_form_title = models.CharField(max_length=255, blank=True, null=True)
    section1_form_description = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if BeAPartnerPage.objects.exists() and not self.pk:
            raise ValidationError('Only one BeAPartnerPage registration is allowed.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Be a partner Page'