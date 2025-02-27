from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

from bookings.choices import TITLE_CHOICES

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email