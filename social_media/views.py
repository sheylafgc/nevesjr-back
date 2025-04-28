from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SocialMedia
from .serializers import SocialMediaSerializer

from django.utils.translation import activate

from drf_yasg.utils import swagger_auto_schema


class SocialMediaAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna as redes sociais passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.query_params.get('lang')

        if not lang:
            return Response({'error': 'The ‘lang’ parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        social_medias = SocialMedia.objects.all()
        if not social_medias.exists():
            return Response({'detail': 'SocialMedia not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SocialMediaSerializer(social_medias, many=True)

        data = [
            {
                'icon': item['icon'],
                'label': item.get(f'label_{lang}', ''),
                'value': item['value'],
            }
            for item in serializer.data
        ]

        return Response(data, status=status.HTTP_200_OK)
