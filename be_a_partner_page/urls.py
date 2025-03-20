from django.urls import path

from .views import *

app_name = 'be_a_partner_page'

urlpatterns = [
    path('be-a-partner-page/', BeAPartnerPageAPIView.as_view(), name='be-a-partner-page-list'),
]