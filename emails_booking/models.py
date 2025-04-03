from django.db import models
from django.core.exceptions import ValidationError


class EmailRaceHiring(models.Model):
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if EmailRaceHiring.objects.exists() and not self.pk:
            raise ValidationError("Only one EmailRaceHiring registration is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Confirmation email for the race"

class EmailRaceFinish(models.Model):
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if EmailRaceFinish.objects.exists() and not self.pk:
            raise ValidationError("Only one EmailRaceFinish registration is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Race completion confirmation email"