from rest_framework import serializers
from .models import AboutPage, TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'avatar']

class AboutPageSerializer(serializers.ModelSerializer):
    team_members = TeamMemberSerializer(many=True)

    class Meta:
        model = AboutPage
        fields = [
            'id',
            'section1_title',
            'section1_subtitle',
            'section1_video',
            'section2_title',
            'section2_description',
            'section3_image',
            'section3_title',
            'section3_description',
            'section4_image',
            'section4_title',
            'section4_description',
            'section5_title', 
            'section5_description',
            'team_members',
            'section6_title',
            'section6_banner', 
        ]
