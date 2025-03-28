from django.urls import path

from .views import *

app_name = 'forgot-password'


urlpatterns = [
    path('create/forgot-password/', ForgotPasswordAPIView.as_view(), name='create-forgot-password'),
    path('validate/forgot-password/', UserResetPasswordExpirateAPIView.as_view(), name='validate-forgot-password'),
    path('new-password/<int:pk>/', NewPasswordAPIView.as_view(), name='create-new-password'),
    path('user-pass-code/', UserResetPasswordListAPIView.as_view(), name='create-new-password'),
]