from django.urls import path

from .views import *

app_name = 'social_media'

urlpatterns = [
    path('social-media/', SocialMediaAPIView.as_view(), name='social-media-list'),
]