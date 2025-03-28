from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Feedback
from .serializers import FeedbackSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class FeedbackListAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna todos os feedbacks'
    )
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
    
class FeedbackCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Cria um feedback',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do usuário'),
                'occupation': openapi.Schema(type=openapi.TYPE_STRING, description='Profissão do usuário'),
                'user_image': openapi.Schema(type=openapi.TYPE_FILE, description='Imagem do usuário'),
                'opinion': openapi.Schema(type=openapi.TYPE_STRING, description='Opinião do usuário'),
            },
        ),
        responses={
            201: '',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FeedbackDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna um feedback'
    )
    def get(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)