from django.urls import path
from .views import *

app_name = 'bookings'

urlpatterns = [
    path('booking/', BookingListAPIView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking-detail'),
    path('booking/create/', BookingCreateAPIView.as_view(), name='booking-create'),
    path('booking/update/', BookingUpdateAPIView.as_view(), name='booking-update'),
    path('booking/delete/', BookingDeleteAPIView.as_view(), name='booking-delete'),
]
