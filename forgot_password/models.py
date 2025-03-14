import uuid
from django.conf import settings
from django.db import models


class UserResetPassword(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_pass_code", blank=True, null=True)
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    generate_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        user_email = self.user.email if self.user else "User not defined"
        return f"Reset password generated for the user {user_email}."