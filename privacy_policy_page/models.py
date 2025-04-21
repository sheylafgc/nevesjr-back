from django.db import models
from django.core.exceptions import ValidationError


class PrivacyPolicyPage(models.Model):
    content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if PrivacyPolicyPage.objects.exists() and not self.pk:
            raise ValidationError('Only one PrivacyPolicyPage registration is allowed.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Privacy Policy Page'