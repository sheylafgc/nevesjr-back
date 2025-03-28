from rest_framework import serializers

from .models import OurServicesPage
from our_services.serializers import OurServiceSerializer


class OurServicesPageSerializer(serializers.ModelSerializer):
    section2_services = OurServiceSerializer(many=True)

    class Meta:
        model = OurServicesPage
        fields = '__all__'