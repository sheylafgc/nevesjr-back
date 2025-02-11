from rest_framework import serializers

from .models import BePartner


class BePartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BePartner
        fields = '__all__'