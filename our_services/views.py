from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OurService
from .serializers import OurServiceSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.utils.translation import activate
from django.shortcuts import get_object_or_404


class OurServiceListAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna todos os serviços passando o idioma como parâmetro"
    )
    def get(self, request):
        lang = request.GET.get("lang")

        if not lang:
            return Response({"error": "The ‘lang’ parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        services = OurService.objects.all()
        services_data = [
            {
                "id": service.id,
                "title": getattr(service, f"title_{lang}", service.title),
                "subtitle": getattr(service, f"subtitle_{lang}", service.subtitle),
                "description": getattr(service, f"description_{lang}", service.description),
                "image": service.image.url if service.image else None,
            }
            for service in services
        ]

        return Response(services_data, status=status.HTTP_200_OK)
    
class OurServiceCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Cria um serviço",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description="Título do serviço"),
                'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description="Subtítulo do serviço"),
                'image': openapi.Schema(type=openapi.TYPE_FILE, description="Imagem do serviço"),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description="Descrição do serviço"),
            },
        ),
        responses={
            201: "",
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = OurServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OurServiceDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna um serviço passando o idioma como parâmetro"
    )
    def get(self, request, pk):
        lang = request.GET.get("lang")

        if not lang:
            return Response({"error": "The ‘lang’ parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        service = get_object_or_404(OurService, pk=pk)

        service_data = {
            "id": service.id,
            "title": getattr(service, f"title_{lang}", service.title),
            "subtitle": getattr(service, f"subtitle_{lang}", service.subtitle),
            "description": getattr(service, f"description_{lang}", service.description),
            "image": service.image.url if service.image else None,
        }

        return Response(service_data, status=status.HTTP_200_OK)

class OurServiceUpdateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Atualiza um serviço",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'subtitle': openapi.Schema(type=openapi.TYPE_STRING),
                'image': openapi.Schema(type=openapi.TYPE_FILE),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            }, 
        ),
        responses={
            200: "",
        }, 
    )
    def put(self, request, pk):
        try:
            ourService = OurService.objects.get(pk=pk)
        except OurService.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurServiceSerializer(ourService, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OurServiceDeleteAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Deleta um serviço"
    )
    def delete(self, request, pk):
        ourService = OurService.objects.get(pk=pk)
        ourService.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)