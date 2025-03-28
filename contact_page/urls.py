from django.urls import path

from .views import *

app_name = 'contact_page'


urlpatterns = [
    path('contact-page/', ContactPageAPIView.as_view(), name='contact-page'),
]