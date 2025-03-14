from rest_framework import serializers

from .models import UserResetPassword

class UserResetPasswordSerializer(serializers.ModelSerializer):
    code = serializers.UUIDField(format='hex_verbose')

    class Meta:
        model = UserResetPassword
        fields = '__all__'