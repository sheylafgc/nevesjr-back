from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    vehicle_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Booking
        fields = '__all__'
        
    def to_internal_value(self, data):
        user = self.context.get('request').user if 'request' in self.context else None

        if data.get('booking_for') == 'myself' and user:
            data = data.copy()
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['email'] = user.email
            data['phone_number'] = user.phone
            data['title'] = user.title

        return super().to_internal_value(data)
    
    def get_vehicle_details(self, obj):
        if obj.vehicle:
            return {
                "car_name": obj.vehicle.car_name,
                "car_type": obj.vehicle.car_type,
                "car_image": obj.vehicle.car_image.url if obj.vehicle.car_image else None
            }
        return None