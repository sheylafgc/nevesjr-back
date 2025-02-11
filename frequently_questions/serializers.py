from rest_framework import serializers

from .models import FrequentlyQuestions


class FrequentlyQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyQuestions
        fields = '__all__'