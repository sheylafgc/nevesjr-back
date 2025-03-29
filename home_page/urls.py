from django.urls import path

from .views import *

app_name = 'home_page'


urlpatterns = [
    path('home-page/', HomePageAPIView.as_view(), name='home-page'),
]