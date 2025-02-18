from django.db import models


class Blog(models.Model):
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title