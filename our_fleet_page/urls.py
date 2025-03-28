from django.urls import path

from .views import *

app_name = 'our_fleet_page'


urlpatterns = [
    path('our-fleet-page/', OurFleetPageAPIView.as_view(), name='our-fleet-page'),
]