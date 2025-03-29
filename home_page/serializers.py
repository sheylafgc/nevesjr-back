from rest_framework import serializers

from .models import HomePageDifferentials, HomePage
from our_services.serializers import OurServiceSerializer
from feedback.serializers import FeedbackSerializer
from vehicles.serializers import VehicleSerializer
from frequently_questions.serializers import FrequentlyQuestionsSerializer


class HomePageDifferentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageDifferentials
        fields = ['id', 'title', 'description']

class HomePageSerializer(serializers.ModelSerializer):
    differentials = HomePageDifferentialsSerializer(many=True)
    section2_services = OurServiceSerializer(many=True)
    section5_feedbacks = FeedbackSerializer(many=True)
    section6_vehicles = VehicleSerializer(many=True)
    section7_frequently_questions = FrequentlyQuestionsSerializer(many=True)

    class Meta:
        model = HomePage
        fields = [
            'section1_banner',
            'section1_title',
            'section2_title',
            'section2_image',
            'section2_services',
            'section3_title',
            'section3_image',
            'differentials',
            'section4_image',
            'section4_title',
            'section4_description',
            'section5_title',
            'section5_subtitle',
            'section5_feedbacks',
            'section6_title',
            'section6_subtitle',
            'section6_vehicles',
            'section7_title',
            'section7_frequently_questions',
            'section8_title',
            'section8_banner',
        ]