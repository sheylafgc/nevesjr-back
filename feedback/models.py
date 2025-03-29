from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    user_image = models.ImageField(upload_to='feedback/user_image', blank=True, null=True)
    opinion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name