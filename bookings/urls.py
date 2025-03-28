from django.urls import path
from .views import *

app_name = 'bookings'


urlpatterns = [
    path('booking/', BookingListAPIView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking-detail'),
    path('booking/create/', BookingCreateAPIView.as_view(), name='booking-create'),
    path('booking/update/<int:pk>/', BookingUpdateAPIView.as_view(), name='booking-update'),
    path('booking/delete/<int:pk>/', BookingDeleteAPIView.as_view(), name='booking-delete'),
    path('booking/cancel/<int:booking_id>/', BookingCancelAPIView.as_view(), name='booking-cancel'),
    path('booking/user/<int:user_id>/', BookingByUserAPIView.as_view(), name='bookings-by-user'),
    path('booking/canceled/user/<int:user_id>/', BookingCanceledByUseAPIView.as_view(), name='canceled-bookings-by-user'),
    path('booking/future/user/<int:user_id>/', BookingFutureByUserAPIView.as_view(), name='canceled-bookings-by-user'),
    path('booking/past/user/<int:user_id>/', BookingPastByUserAPIView.as_view(), name='canceled-bookings-by-user'),
]
