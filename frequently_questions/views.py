from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FrequentlyQuestions
from .serializers import FrequentlyQuestionsSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class FrequentlyQuestionsListAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna todas os perguntas frequentes'
    )
    def get(self, request):
        frequentlyQuestions = FrequentlyQuestions.objects.all()
        serializer = FrequentlyQuestionsSerializer(frequentlyQuestions, many=True)
        return Response(serializer.data)
    
class FrequentlyQuestionsCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Cria uma pergunta frequente',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING, description='Pergunta frequente'),
                'answer': openapi.Schema(type=openapi.TYPE_STRING, description='Resposta'),
            },
        ),
        responses={
            201: '',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = FrequentlyQuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FrequentlyQuestionsDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna uma pergunta frequente'
    )
    def get(self, request, pk):
        frequentlyQuestions = FrequentlyQuestions.objects.get(pk=pk)
        serializer = FrequentlyQuestionsSerializer(frequentlyQuestions)
        return Response(serializer.data)
    
class FrequentlyQuestionsUpdateAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Atualiza uma pergunta frequente',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'question': openapi.Schema(type=openapi.TYPE_STRING, description='Pergunta frequente'),
                'answer': openapi.Schema(type=openapi.TYPE_STRING, description='Resposta'),
            },
        ),
        responses={
            200: '',
        }, 
    )
    def put(self, request, pk):
        try:
            frequentlyQuestions = FrequentlyQuestions.objects.get(pk=pk)
        except FrequentlyQuestions.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FrequentlyQuestionsSerializer(frequentlyQuestions, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FrequentlyQuestionsDeleteAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Deleta uma pergunta frequente'
    )
    def delete(self, request, pk):
        frequentlyQuestions = FrequentlyQuestions.objects.get(pk=pk)
        frequentlyQuestions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)