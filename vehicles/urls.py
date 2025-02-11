from django.urls import path

from .views import *

app_name = 'vehicle'

urlpatterns = [
    path('vehicle', VehicleListAPIView.as_view(), name='vehicle-list'),
    path('vehicle/<int:pk>', VehicleDetailAPIView.as_view(), name='vehicle-detail'),
    path('vehicle/create', VehicleCreateAPIView.as_view(), name='vehicle-create'),
    path('vehicle/update/<int:pk>', VehicleUpdateAPIView.as_view(), name='vehicle-update'),
    path('vehicle/delete/<int:pk>', VehicleDeleteAPIView.as_view(), name='vehicle-delete'),
]