from rest_framework import serializers

from .models import PrivacyPolicyPage


class PrivacyPolicyPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicyPage
        fields = '__all__'