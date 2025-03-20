from rest_framework import serializers

from .models import BeAPartnerPage


class BeAPartnerPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeAPartnerPage
        fields = '__all__'
