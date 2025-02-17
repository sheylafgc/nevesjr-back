from django.db import models

class OurService(models.Model):
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/ourServices/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title