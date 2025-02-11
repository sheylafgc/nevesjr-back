from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vehicle
from .serializers import VehicleSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class VehicleListAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna todos os veículos da frota"
    )
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
class VehicleCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Cria um novo veículo",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'car_name': openapi.Schema(type=openapi.TYPE_STRING, description="Marca e model do veículo"),
                'car_type': openapi.Schema(type=openapi.TYPE_STRING, description="Tipo do veículo"),
                'quantity_seats': openapi.Schema(type=openapi.TYPE_STRING, description="Quantidade de assentos do veículo"),
                'quantity_luggage': openapi.Schema(type=openapi.TYPE_STRING, description="Quantidade de bagagens que o veículo suporta"),
                'car_image': openapi.Schema(type=openapi.TYPE_FILE, description="Imagem do veículo"),
                'price': openapi.Schema(type=openapi.TYPE_FILE, description="Preço do veículo na viagem"),
                'car_overview': openapi.Schema(type=openapi.TYPE_STRING, description="Overview do veículo"),
                'car_amenities': openapi.Schema(type=openapi.TYPE_STRING, description="Comodidades do veículo"),
                'car_best_for_services': openapi.Schema(type=openapi.TYPE_STRING, description="O melhor para estes serviços"),
            },
        ),
        responses={
            201: "",
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehicleDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna um veículo"
    )
    def get(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    
class VehicleUpdateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Atualiza um veículo",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'car_name': openapi.Schema(type=openapi.TYPE_STRING, description="Marca e model do veículo"),
                'car_type': openapi.Schema(type=openapi.TYPE_STRING, description="Tipo do veículo"),
                'quantity_seats': openapi.Schema(type=openapi.TYPE_STRING, description="Quantidade de assentos do veículo"),
                'quantity_luggage': openapi.Schema(type=openapi.TYPE_STRING, description="Quantidade de bagagens que o veículo suporta"),
                'car_image': openapi.Schema(type=openapi.TYPE_FILE, description="Imagem do veículo"),
                'price': openapi.Schema(type=openapi.TYPE_FILE, description="Preço do veículo na viagem"),
                'car_overview': openapi.Schema(type=openapi.TYPE_STRING, description="Overview do veículo"),
                'car_amenities': openapi.Schema(type=openapi.TYPE_STRING, description="Comodidades do veículo"),
                'car_best_for_services': openapi.Schema(type=openapi.TYPE_STRING, description="O melhor para estes serviços"),
            },
        ),
        responses={
            200: "",
        }, 
    )
    def put(self, request, pk):
        try:
            vehicle = Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehicleDeleteAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Deleta um veículo"
    )
    def delete(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)