from rest_framework import serializers

from .models import OurFleetPage
from vehicles.serializers import VehicleSerializer


class OurFleetPageSerializer(serializers.ModelSerializer):
    section2_vehicles = VehicleSerializer(many=True)

    class Meta:
        model = OurFleetPage
        fields = '__all__'