from rest_framework import serializers

from .models import SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('phone_whatsapp1', 'phone_whatsapp2', 'email', 'facebook', 'instagram', 'x')