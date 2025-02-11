from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    email = models.EmailField(blank=True, null=False)
    message = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.email