from decimal import Decimal
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import stripe

from django.conf import settings

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentReceiptView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Passando o id do pagamento retorna o comprovante do pagamento"
    )
    def get(self, request, payment_intent_id, *args, **kwargs):
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

            charge_id = payment_intent.latest_charge
            charge = stripe.Charge.retrieve(charge_id)

            return Response(
                {
                    "receipt_url": charge.receipt_url,
                },
                status=status.HTTP_200_OK
            )

        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
