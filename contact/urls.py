from django.urls import path

from .views import *

app_name = 'contact'

urlpatterns = [
    path('contact', ContactListAPIView.as_view(), name='contact-list'),
    path('contact/<int:pk>', ContactDetailAPIView.as_view(), name='contact-detail'),
    path('contact/create', ContactCreateAPIView.as_view(), name='contact-create'),
]