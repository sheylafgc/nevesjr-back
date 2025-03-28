from django.urls import path
from .views import *

app_name = 'payments'


urlpatterns = [
    path('payment/receipt/<str:payment_intent_id>', PaymentReceiptView.as_view(), name='payment-intent'),
]
