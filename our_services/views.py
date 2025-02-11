from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OurService
from .serializers import OurServiceSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class OurServiceListAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna todos os serviços"
    )
    def get(self, request):
        ourServices = OurService.objects.all()
        serializer = OurServiceSerializer(ourServices, many=True)
        return Response(serializer.data)
    
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
        operation_description="Retorna um serviço"
    )
    def get(self, request, pk):
        ourService = OurService.objects.get(pk=pk)
        serializer = OurServiceSerializer(ourService)
        return Response(serializer.data)
    
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