from decimal import ROUND_DOWN, Decimal
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import Booking

from .serializers import BookingSerializer

import stripe

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

stripe.api_key = settings.STRIPE_SECRET_KEY

class BookingListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="Retorna todos as reservas"
    )
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

class BookingCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Criar uma reserva",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(type=openapi.TYPE_STRING, description="ID do usuário"),
                'from_route': openapi.Schema(type=openapi.TYPE_STRING, description="Ponto de partida"),
                'to_route': openapi.Schema(type=openapi.TYPE_STRING, description="Destino final"),
                'date': openapi.Schema(type=openapi.TYPE_STRING, description="Data da reserva - (2025-01-01)"),
                'hour': openapi.Schema(type=openapi.TYPE_STRING, description="Hora da reserva - (15:00:00)"),
                'duration': openapi.Schema(type=openapi.TYPE_STRING, description="Duração da reserva caso não tenha destino final definido - (01:00:00)"),
                'estimated_time': openapi.Schema(type=openapi.TYPE_STRING, description="Tempo estimado do ponto de partida até o destino final - (16:00:00)"),
                'distance_km': openapi.Schema(type=openapi.TYPE_INTEGER, description="Distância entre o ponto de partida e o destino final - (10), se não for passado valor, passar como 0"),
                'vehicle': openapi.Schema(type=openapi.TYPE_INTEGER, description="Veiculo escolhido na reserva - (id do veículo)"),
                'booking_for': openapi.Schema(type=openapi.TYPE_STRING, description="Para quem será a reserva - (myself ou someone_else)"),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description="Primeiro nome"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description="Segundo nome"),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email"),
                'title': openapi.Schema(type=openapi.TYPE_STRING, description="Titulo - (Mr ou Ms)"),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description="Número de telefone"),
                'notes': openapi.Schema(type=openapi.TYPE_STRING, description="Observações"),
            },
        ),
        responses={
            201: "",
        }, 
    )
    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        amount = 0

        try:
            user = request.user
            email = user.email

            if not email:
                return Response({'error': 'Usuário não possui um e-mail cadastrado'}, status=status.HTTP_400_BAD_REQUEST)

            vehicle = validated_data.get('vehicle')
            distance_km = validated_data.get('distance_km')
            duration = validated_data.get('duration')
            to_route = validated_data.get('to_route')

            if to_route and duration:
                return Response(
                    {'error': "Se 'to_route' está presente, 'duration' não pode ser fornecido."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not to_route and distance_km:
                return Response(
                    {'error': "Se 'to_route' não está presente, 'distance_km' não pode ser fornecido."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if vehicle:
                if to_route and vehicle.price_km and distance_km:
                    amount = (vehicle.price_km * Decimal(str(distance_km)) * 100).quantize(Decimal("1"), rounding=ROUND_DOWN)
                elif not to_route and vehicle.price_hour and duration:
                    duration_hours = Decimal(duration.total_seconds()) / Decimal(3600)
                    amount = (vehicle.price_hour * duration_hours * 100).quantize(Decimal("1"), rounding=ROUND_DOWN)

            existing_customers = stripe.Customer.list(email=email).data
            if existing_customers:
                customer = existing_customers[0]
            else:
                customer = stripe.Customer.create(
                    email=email,
                    name=f"{user.first_name} {user.last_name}",
                )

            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency='gbp',
                customer=customer.id,
                payment_method_types=["card"],
                automatic_payment_methods={"enabled": False},
                metadata={
                    **validated_data,
                    'amount': str(amount),
                    'vehicle': str(vehicle.id) if vehicle else None,
                    'user_id': str(user.id)
                }
            )

            return Response({
                'client_secret': payment_intent['client_secret'],
                'payment_intent_id': payment_intent.id
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BookingDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retorna uma reserva"
    )
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

class BookingUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="Atualiza uma reserva",
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
        operation_description="Deleta uma reserva"
    )
    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response({"message": "Booking deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class BookingCancelAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Cancela uma reserva"
    )
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)

        if booking.payment_status != 'approved':
            return Response({'error': 'Booking não pode ser cancelado, pois o pagamento não foi aprovado.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refund = stripe.Refund.create(
                payment_intent=booking.payment_intent_id,
            )

            booking.payment_status = 'canceled'
            booking.save()

            return Response({'status': 'Booking cancelado e reembolso realizado com sucesso.'}, status=status.HTTP_200_OK)

        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class BookingByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Lista as reservas de um determinado usuário"
    )
    def get(self, request, user_id):
        bookings = Booking.objects.filter(user_id=user_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CanceledBookingsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Lista as reservas do usuário com status cancelado"
    )
    def get(self, request, user_id):
        bookings = Booking.objects.filter(user_id=user_id, payment_status='canceled')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)