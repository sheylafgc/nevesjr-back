from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SocialMedia
from .serializers import SocialMediaSerializer

from drf_yasg.utils import swagger_auto_schema


class SocialMediaAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna todos as redes sociais"
    )
    def get(self, request):
        socialMedia = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(socialMedia, many=True)
        return Response(serializer.data)
