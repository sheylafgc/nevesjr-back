from django.urls import path

from .views import *

app_name = 'be-partner'

urlpatterns = [
    path('be-partner', BePartnerListAPIView.as_view(), name='be-partner-list'),
    path('be-partner/<int:pk>', BePartnerDetailAPIView.as_view(), name='be-partner-detail'),
    path('be-partner/create', BePartnerCreateAPIView.as_view(), name='be-partner-create'),
]