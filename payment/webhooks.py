from datetime import timedelta, datetime

from decimal import Decimal

import pytz
import stripe

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from rest_framework import status

from bookings.models import Booking
from users.models import User


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError:
        return JsonResponse({'error': 'Invalid payload'}, status=status.HTTP_400_BAD_REQUEST)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'error': 'Invalid signature'}, status=status.HTTP_400_BAD_REQUEST)
    
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        metadata = payment_intent['metadata']
        vehicle_id = metadata.get('vehicle')
        user_id = metadata.get('user_id') 

        duration_str = metadata.get('duration')
        duration = None

        if duration_str:
            try:
                hours, minutes, seconds = map(int, duration_str.split(':'))
                duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            except ValueError:
                duration = None 

        date_str = metadata.get('date')
        if date_str.isdigit():
            date = datetime.fromtimestamp(int(date_str), tz=pytz.UTC)
        else:
            date = date_str

        payment_intent = stripe.PaymentIntent.retrieve(payment_intent['id'])

        charge_id = payment_intent.latest_charge
        charge = stripe.Charge.retrieve(charge_id)

        user = User.objects.get(id=user_id)

        booking = Booking.objects.create(
            from_route=metadata.get('from_route'),
            to_route=metadata.get('to_route'),
            date=date,
            hour=metadata.get('hour'),
            duration=duration,
            estimated_time=metadata.get('estimated_time'),
            distance_km=metadata.get('distance_km'),
            vehicle_id=vehicle_id,
            booking_for=metadata.get('booking_for'),
            first_name=metadata.get('first_name'),
            last_name=metadata.get('last_name'),
            title=metadata.get('title'),
            email=metadata.get('email'),
            phone_number=metadata.get('phone_number'),
            notes=metadata.get('notes'),
            amount=Decimal(metadata.get('amount', '0')),
            payment_intent_id=payment_intent['id'],
            payment_status='approved',
            payment_brand=charge.payment_method_details.card.brand,
            user=user,
        )

    return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)