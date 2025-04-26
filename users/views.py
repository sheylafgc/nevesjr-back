from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import User
from emails.send_email_activate_user import send_email_activate_user

from drf_yasg.utils import swagger_auto_schema


class UserListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Retorna todos os usuários'
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        operation_description='Cria um usuário',
        responses={
            201: '',
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            send_email_activate_user(
                email=user.email,
                first_name=user.first_name,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Retorna um usuário'
    )
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=UserSerializer, 
        operation_description='Atualiza um usuário',
        responses={
            200: '',
        }, 
    )
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Deleta um usuário'
    )
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Retorna o perfil de um usuário'
    )
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetUserIdByEmailView(APIView):
    def get(self, request, email):
        user = get_object_or_404(User, email=email)
        return Response({'id': user.id}, status=status.HTTP_200_OK)
    
class ActivateUserAPIView(APIView):
    def get(self, request, email):
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                return Response({'detail': 'User is already active.'}, status=status.HTTP_404_NOT_FOUND)
            
            user.is_active = True
            user.save()
            return Response({'detail': 'User successfully activated.'}, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)