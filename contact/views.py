from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contact
from .serializers import ContactSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ContactListAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna todos os contatos'
    )
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
class ContactCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Cria um contato',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do usuário'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email do usuário'),
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem do usuário'),
            },
        ),
        responses={
            201: '',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna um contato'
    )
    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)