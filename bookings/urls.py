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
    path('booking/cancel/admin/<int:booking_id>/', BookingCancelAPIView.as_view(), name='booking-admin-cancel'),
    path('booking/user/<int:user_id>/', BookingByUserAPIView.as_view(), name='bookings-by-user'),
    path('booking/canceled/user/<int:user_id>/', BookingCanceledByUserAPIView.as_view(), name='canceled-bookings-by-user'),
    path('booking/canceled/admin/', BookingCanceledAdminListAPIView.as_view(), name='canceled-bookings-admin-list'),
    path('booking/future/user/<int:user_id>/', BookingFutureByUserAPIView.as_view(), name='future-bookings-by-user'),
    path('booking/past/user/<int:user_id>/', BookingPastByUserAPIView.as_view(), name='canceled-bookings-by-user'),
    path('booking/future/admin/', BookingFutureAdminListAPIView.as_view(), name='future-bookings-admin-list'),
    path('booking/past/admin/', BookingPastAdminListAPIView.as_view(), name='canceled-bookings-admin-list'),
    path('booking/finish/', BookingUpdateStatusAdminAPIView.as_view(), name='booking-finish-race'),
]
