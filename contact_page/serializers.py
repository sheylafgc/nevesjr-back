from rest_framework import serializers

from .models import ContactPage
from social_media.serializers import SocialMediaSerializer


class ContactPageSerializer(serializers.ModelSerializer):
    section1_social_media = SocialMediaSerializer()

    class Meta:
        model = ContactPage
        fields = '__all__'