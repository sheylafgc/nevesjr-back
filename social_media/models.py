from django.db import models
from django.core.exceptions import ValidationError

import os


def validate_svg(file):
    ext = os.path.splitext(file.name)[1]
    if ext.lower() != ".svg":
        raise ValidationError("Somente arquivos SVG são permitidos.")

class SocialMedia(models.Model):
    icon = models.FileField(upload_to='social_media/icons/', validators=[validate_svg], blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.label if self.label else "Social Media"