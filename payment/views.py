from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import stripe
import pdfkit

from django.conf import settings
from django.http import HttpResponse

from drf_yasg.utils import swagger_auto_schema

import requests

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentReceiptView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Passando o id do pagamento retorna o comprovante do pagamento em pdf'
    )
    def get(self, request, payment_intent_id, *args, **kwargs):
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

            charge_id = payment_intent.latest_charge
            charge = stripe.Charge.retrieve(charge_id)

            receipt_url = charge.receipt_url

            response = requests.get(receipt_url)
            response.raise_for_status()

            pdf = pdfkit.from_string(response.text, False)

            pdf_response = HttpResponse(pdf, content_type='application/pdf')
            pdf_response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'
            return pdf_response

        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except requests.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)