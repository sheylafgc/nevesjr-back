from django.urls import path

from .views import *

app_name = 'feedback'

urlpatterns = [
    path('feedback', FeedbackListAPIView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>', FeedbackDetailAPIView.as_view(), name='feedback-detail'),
    path('feedback/create', FeedbackCreateAPIView.as_view(), name='feedback-create'),
]