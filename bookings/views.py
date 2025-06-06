from decimal import ROUND_DOWN, Decimal

from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from django.shortcuts import get_object_or_404

from datetime import timedelta, datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer
from emails.send_email_admin_race import send_email_admin_pending_race
from emails.send_email_client_race import send_email_admin_approved_race
from emails.send_email_cancel_race import send_email_admin_cancel_race, send_email_user_cancel_race

from emails_booking.emails import send_email_template
from emails_booking.models import EmailRaceFinish, EmailRaceHiring

import stripe

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

stripe.api_key = settings.STRIPE_SECRET_KEY


class BookingListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Retorna todos as reservas'
    )
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

class BookingCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Criar uma reserva',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(type=openapi.TYPE_STRING, description='ID do usuário'),
                'from_route': openapi.Schema(type=openapi.TYPE_STRING, description='Ponto de partida'),
                'to_route': openapi.Schema(type=openapi.TYPE_STRING, description='Destino final'),
                'date': openapi.Schema(type=openapi.TYPE_STRING, description='Data da reserva - (2025-01-01)'),
                'hour': openapi.Schema(type=openapi.TYPE_STRING, description='Hora da reserva - (15:00:00)'),
                'duration': openapi.Schema(type=openapi.TYPE_STRING, description='Duração da reserva caso não tenha destino final definido - (01:00:00)'),
                'estimated_time': openapi.Schema(type=openapi.TYPE_STRING, description='Tempo estimado do ponto de partida até o destino final - (16:00:00)'),
                'distance_km': openapi.Schema(type=openapi.TYPE_INTEGER, description='Distância entre o ponto de partida e o destino final - (10), se não for passado valor, passar como 0'),
                'vehicle': openapi.Schema(type=openapi.TYPE_INTEGER, description='Veiculo escolhido na reserva - (id do veículo)'),
                'booking_for': openapi.Schema(type=openapi.TYPE_STRING, description='Para quem será a reserva - (myself ou someone_else)'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Primeiro nome'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Segundo nome'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Titulo - (Mr ou Ms)'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Número de telefone'),
                'notes': openapi.Schema(type=openapi.TYPE_STRING, description='Observações'),
            },
        ),
        responses={
            201: '',
        }, 
    )
    # def post(self, request):
    #     serializer = BookingSerializer(data=request.data, context={'request': request})

    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     validated_data = serializer.validated_data
    #     amount = 0

    #     try:
    #         user = request.user
    #         email = user.email

    #         if not email:
    #             return Response({'error': 'User does not have a registered e-mail address.'}, status=status.HTTP_400_BAD_REQUEST)

    #         vehicle = validated_data.get('vehicle')
    #         distance_km = validated_data.get('distance_km')
    #         duration = validated_data.get('duration')
    #         to_route = validated_data.get('to_route')

    #         if to_route and duration:
    #             return Response(
    #                 {'error': 'If ‘to_route’ is present, ‘duration’ cannot be supplied.'},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )
    #         if not to_route and distance_km:
    #             return Response(
    #                 {'error': 'If ‘to_route’ is not present, ‘distance_km’ cannot be supplied.'},
    #                 status=status.HTTP_400_BAD_REQUEST
    #             )

    #         if vehicle:
    #             if to_route and vehicle.price_km and distance_km:
    #                 amount = (vehicle.price_km * Decimal(str(distance_km)) * 100).quantize(Decimal('1'), rounding=ROUND_DOWN)
    #             elif not to_route and vehicle.price_hour and duration:
    #                 duration_hours = Decimal(duration.total_seconds()) / Decimal(3600)
    #                 amount = (vehicle.price_hour * duration_hours * 100).quantize(Decimal('1'), rounding=ROUND_DOWN)

    #         existing_customers = stripe.Customer.list(email=email).data
    #         if existing_customers:
    #             customer = existing_customers[0]
    #         else:
    #             customer = stripe.Customer.create(
    #                 email=email,
    #                 name=f'{user.first_name} {user.last_name}',
    #             )

    #         payment_intent = stripe.PaymentIntent.create(
    #             amount=int(amount),
    #             currency='gbp',
    #             customer=customer.id,
    #             payment_method_types=['card'],
    #             automatic_payment_methods={'enabled': False},
    #             metadata={
    #                 **validated_data,
    #                 'amount': str(amount),
    #                 'vehicle': str(vehicle.id) if vehicle else None,
    #                 'user_id': str(user.id)
    #             }
    #         )

    #         return Response({
    #             'client_secret': payment_intent['client_secret'],
    #             'payment_intent_id': payment_intent.id
    #         }, status=status.HTTP_201_CREATED)

    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data.copy()
        data['booking_status'] = 'pending'

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            booking = serializer.save()
            
            if booking.email:
                send_email_admin_pending_race(
                    client_name=booking.first_name,
                    date_booking=booking.date,
                    hour_booking=booking.hour,
                    from_route=booking.from_route,
                    to_route=booking.to_route,
                    vehicle_class=booking.vehicle.car_type,
                    notes=booking.notes,
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Retorna uma reserva'
    )
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

class BookingUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Atualiza uma reserva',
    )
    def put(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Deleta uma reserva'
    )
    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response({'message': 'Booking successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class BookingCancelUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Cancela uma reserva'
    )
    # def post(self, request, booking_id):
    #     booking = get_object_or_404(Booking, id=booking_id)

    #     if booking.payment_status != 'approved':
    #         return Response({'error': 'Booking cannot be cancelled because payment has not been approved.'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     if booking.booking_status != 'upcoming':
    #         return Response({'error': 'Booking can only be cancelled if it is in "upcoming" status.'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     current_time = timezone.now().time()
    #     booking_hour = booking.hour 

    #     current_datetime = timezone.now().replace(hour=current_time.hour, minute=current_time.minute, second=current_time.second, microsecond=0)
    #     booking_datetime = timezone.now().replace(hour=booking_hour.hour, minute=booking_hour.minute, second=booking_hour.second, microsecond=0)

    #     if current_datetime - booking_datetime > timedelta(hours=2):
    #         return Response({'error': 'Booking cannot be cancelled because it is 2 hours or more past the scheduled time.'}, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         refund = stripe.Refund.create(
    #             payment_intent=booking.payment_intent_id,
    #         )

    #         booking.payment_status = 'canceled'
    #         booking.booking_status = 'canceled'
    #         booking.save()

    #         return Response({'status': 'Booking cancelled and refund successful.'}, status=status.HTTP_200_OK)

    #     except stripe.error.StripeError as e:
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)

        if booking.booking_status not in ['upcoming', 'pending']:
            return Response({'error': 'Booking can only be cancelled if it is in "upcoming" or "pending" status.'}, status=status.HTTP_400_BAD_REQUEST)

        if not booking.date or not booking.hour:
            return Response({'error': 'Booking date or hour is not set.'}, status=status.HTTP_400_BAD_REQUEST)

        booking_datetime = datetime.combine(booking.date.date(), booking.hour)
        booking_datetime = timezone.make_aware(booking_datetime, timezone.get_current_timezone())

        current_datetime = timezone.localtime()

        if current_datetime > booking_datetime + timedelta(hours=2):
            return Response({'error': 'Booking cannot be cancelled because it is 2 hours or more past the scheduled time.'}, status=status.HTTP_400_BAD_REQUEST)

        booking.booking_status = 'canceled'
        booking.save()

        send_email_user_cancel_race(
            email=booking.email,
            client_name=booking.first_name,
            date_booking=booking.date,
            hour_booking=booking.hour,
            from_route=booking.from_route,
            to_route=booking.to_route,
            vehicle_class=booking.vehicle.car_type,
        )

        return Response({'status': 'Booking cancelled successfully.'}, status=status.HTTP_200_OK)
    
class BookingCancelAdminAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Cancela uma reserva'
    )
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)

        if booking.booking_status not in ['upcoming', 'pending']:
            return Response({'error': 'Booking can only be cancelled if it is in "upcoming" or "pending" status.'}, status=status.HTTP_400_BAD_REQUEST)

        if not booking.date or not booking.hour:
            return Response({'error': 'Booking date or hour is not set.'}, status=status.HTTP_400_BAD_REQUEST)

        booking_datetime = datetime.combine(booking.date.date(), booking.hour)
        booking_datetime = timezone.make_aware(booking_datetime, timezone.get_current_timezone())

        current_datetime = timezone.localtime()

        if current_datetime > booking_datetime + timedelta(hours=2):
            return Response({'error': 'Booking cannot be cancelled because it is 2 hours or more past the scheduled time.'}, status=status.HTTP_400_BAD_REQUEST)

        booking.booking_status = 'canceled'
        booking.save()

        send_email_admin_cancel_race(
            email=booking.email,
            client_name=booking.first_name,
            date_booking=booking.date,
            hour_booking=booking.hour,
            from_route=booking.from_route,
            to_route=booking.to_route,
            vehicle_class=booking.vehicle.car_type,
        )

        return Response({'status': 'Booking cancelled successfully.'}, status=status.HTTP_200_OK)
        
class BookingByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Lista as reservas de um determinado usuário'
    )
    def get(self, request, user_id):
        bookings = Booking.objects.filter(user_id=user_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingCanceledByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Lista as reservas do usuário com status cancelado'
    )
    def get(self, request, user_id):
        bookings = Booking.objects.filter(user_id=user_id, booking_status='canceled')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingCanceledAdminListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Lista todas as reservas com status cancelado'
    )
    def get(self, request):
        bookings = Booking.objects.filter(booking_status='canceled')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingFutureByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Lista as reservas futuras de um determinado usuário'
    )
    def get(self, request, user_id):
        future_bookings = Booking.objects.filter(
            user_id=user_id, booking_status='upcoming'
        ).exclude(payment_status='canceled')

        serializer = BookingSerializer(future_bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingPastByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Lista as reservas passadas de um determinado usuário'
    )
    def get(self, request, user_id):
        past_bookings = Booking.objects.filter(
            user_id=user_id, booking_status='past'
        ).exclude(payment_status='canceled')

        serializer = BookingSerializer(past_bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingFutureAdminListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Lista todas as reservas futuras'
    )
    def get(self, request):
        future_bookings = Booking.objects.filter(
            booking_status='upcoming'
        ).exclude(payment_status='canceled')

        serializer = BookingSerializer(future_bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingPastAdminListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Lista todas as reservas passadas'
    )
    def get(self, request):
        past_bookings = Booking.objects.filter(
            booking_status='past'
        ).exclude(payment_status='canceled')

        serializer = BookingSerializer(past_bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookingPendingAdminListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='Lista todas as reservas pendentes'
    )
    def get(self, request):
        past_bookings = Booking.objects.filter(
            booking_status='pending'
        ).exclude(payment_status='canceled')

        serializer = BookingSerializer(past_bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingApprovedRaceAdminAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Atualiza o status de uma reserva específica de pending para upcoming'
    )
    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, booking_status='pending')
            booking.booking_status = 'upcoming'
            booking.save()

            amount = f"${booking.amount:.2f}" if booking.amount is not None else "Not specified"
            status_payment = booking.payment_status or "Not specified"
            payment_method = booking.payment_brand or "Not specified"
            payment_date = booking.payment_date.strftime('%B %d, %Y at %I:%M %p') if booking.payment_date else "Not specified"

            payment_instructions = f"""
            Amount: {amount}<br>
            Status: {status_payment}<br>
            Payment method: {payment_method}<br>
            Paid on: {payment_date}
            """

            send_email_admin_approved_race(
                email=booking.user.email,
                client_name=booking.first_name,
                date_booking=booking.date,
                hour_booking=booking.hour,
                from_route=booking.from_route,
                to_route=booking.to_route,
                vehicle_class=booking.vehicle.car_type,
                notes=booking.notes,
                payment_instructions=payment_instructions
            )

            return Response(
                {'message': f"Booking has been updated to 'upcoming'."},
                status=status.HTTP_200_OK
            )

        except Booking.DoesNotExist:
            return Response(
                {'error': "Reservation not found or not in 'pending' status."},
                status=status.HTTP_404_NOT_FOUND
            )
        
class BookingFinishRaceAdminAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Atualiza o status de uma reserva específica de upcoming para past'
    )
    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, booking_status='upcoming')
            booking.booking_status = 'past'
            booking.save()

            email = booking.user.email

            send_email_template(EmailRaceFinish, email)

            return Response(
                {'message': f"Booking has been updated to 'past'."},
                status=status.HTTP_200_OK
            )

        except Booking.DoesNotExist:
            return Response(
                {'error': "Reservation not found or not in 'upcoming' status."},
                status=status.HTTP_404_NOT_FOUND
            )