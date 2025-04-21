from django.urls import path

from .views import *

app_name = 'privacy_policy_page'


urlpatterns = [
    path('privacy-policy-page/', PrivacyPolicyPageAPIView.as_view(), name='privacy-policy-page'),
]