from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import BePartner
from .serializers import BePartnerSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BePartnerListAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna todos as solicitações"
    )
    def get(self, request):
        bePartner = BePartner.objects.all()
        serializer = BePartnerSerializer(bePartner, many=True)
        return Response(serializer.data)
    
class BePartnerCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Cria um formulário para ser parceiro",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description="Nome do usuário"),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="Email do usuário"),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description="Telefone do usuário"),
                'car_model': openapi.Schema(type=openapi.TYPE_STRING, description="Modelo do carro"),
            },
        ),
        responses={
            201: "",
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = BePartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BePartnerDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna uma solicitação"
    )
    def get(self, request, pk):
        bePartner = BePartner.objects.get(pk=pk)
        serializer = BePartnerSerializer(bePartner)
        return Response(serializer.data)