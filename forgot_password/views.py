import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserResetPassword
from users.models import User

from .serializers import UserResetPasswordSerializer
from users.serializers import UserSerializer

from django.contrib.auth.hashers import make_password

from django.utils import timezone

from django.utils import timezone

from emails.send_email_reset_password import send_email_reset_password

from drf_yasg.utils import swagger_auto_schema


class ForgotPasswordAPIView(APIView):
    @swagger_auto_schema(
    operation_description="Gera o email de recuperação de senha"
    )
    def post(self, request, format=None):
        email = request.query_params.get('email', None)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "Email not found in the database."}, status=status.HTTP_404_NOT_FOUND)

        code = uuid.uuid4()
        
        user_pass_code = UserResetPassword.objects.create(
            user=user,
            code=str(code),
            generate_date=timezone.now(),
            expiration_date=timezone.now() + timezone.timedelta(minutes=10),
            active=True
        )
        user_pass_code.save()

        user_name = user.get_full_name() if user.get_full_name() else user.first_name or "User"

        send_email_reset_password(email, user_name, code)

        return Response({"message": "Request generated successfully."}, status=status.HTTP_201_CREATED)
    
class UserResetPasswordExpirateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Valida code e email da requisição"
    )
    def get(self, request):
        code = request.query_params.get("code")
        email = request.query_params.get("email")

        if not email or not code:
            return Response({"detail": "Email and code required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            user_pass_code = UserResetPassword.objects.get(user=user, code=code)
        except UserResetPassword.DoesNotExist:
            return Response({"detail": "Invalid code for this user."}, status=status.HTTP_404_NOT_FOUND)

        if user_pass_code.expiration_date and user_pass_code.expiration_date < timezone.now():
            user_pass_code.active = False
            user_pass_code.save(update_fields=['active'])
            return Response({"detail": "Expired code."}, status=status.HTTP_400_BAD_REQUEST)

        if user_pass_code.active:
            user_pass_code.active = False
            user_pass_code.save(update_fields=['active'])
            return Response({"detail": "Valid code."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Code has been used before."}, status=status.HTTP_400_BAD_REQUEST)
    
class NewPasswordAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Atualiza senha do usuário"
    )
    def put(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')

            if password:
                user.password = make_password(password)

            user.save()
            
            return Response({"message": "Password successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserResetPasswordListAPIView(APIView):
    def get(self, request):
        user_pass_codes = UserResetPassword.objects.all()
        serializer = UserResetPasswordSerializer(user_pass_codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)