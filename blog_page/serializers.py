from rest_framework import serializers

from blog.serializers import BlogSerializer
from .models import BlogPage


class BlogPageSerializer(serializers.ModelSerializer):
    blog_page = BlogSerializer(many=True)

    class Meta:
        model = BlogPage
        fields = '__all__'