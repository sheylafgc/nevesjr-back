from django.urls import path

from .views import *

app_name = 'our_services_page'


urlpatterns = [
    path('our-services-page/', OurServicesPageAPIView.as_view(), name='our-services-page'),
]