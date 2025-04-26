from django.urls import path

from .views import *

app_name = 'users'


urlpatterns = [
    path('user', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
    path('user/create', UserCreateAPIView.as_view(), name='user-create'),
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>', UserDeleteAPIView.as_view(), name='user-delete'),
    path('user/profile', UserProfileAPIView.as_view(), name='user-profile'),
    path('user/id/<str:email>/', GetUserIdByEmailView.as_view(), name='get-user-id'),
    path('user/activate/<str:email>/', ActivateUserAPIView.as_view(), name='activate-user'),
]