from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SocialMedia
from .serializers import SocialMediaSerializer


class SocialMediaAPIView(APIView):
    def get(self, request):
        socialMedia = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(socialMedia, many=True)
        return Response(serializer.data)
