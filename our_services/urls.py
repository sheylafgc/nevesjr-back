from django.urls import path

from .views import *

app_name = 'our-services'

urlpatterns = [
    path('our-service', OurServiceListAPIView.as_view(), name='our-service-list'),
    path('our-service/<int:pk>', OurServiceDetailAPIView.as_view(), name='our-service-detail'),
    path('our-service/create', OurServiceCreateAPIView.as_view(), name='our-service-create'),
    path('our-service/update/<int:pk>', OurServiceUpdateAPIView.as_view(), name='our-service-update'),
    path('our-service/delete/<int:pk>', OurServiceDeleteAPIView.as_view(), name='our-service-delete'),
]