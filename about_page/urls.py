from django.urls import path

from .views import *

app_name = 'about_page'


urlpatterns = [
    path('about-page/', AboutPageAPIView.as_view(), name='about-paget'),
]