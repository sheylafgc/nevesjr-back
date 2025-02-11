from rest_framework import serializers

from .models import OurService

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        # fields = ('id', 'title', 'subtitle', 'image', 'description')
        fields = '__all__'