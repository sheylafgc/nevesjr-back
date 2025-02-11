from django.db import models


class BePartner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    car_model = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email