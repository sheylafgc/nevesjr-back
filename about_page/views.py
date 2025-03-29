from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import AboutPage
from .serializers import AboutPageSerializer

from drf_yasg.utils import swagger_auto_schema


class AboutPageAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna o contéudo da tela About passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.GET.get('lang')

        if not lang:
            return Response({'error': 'The ‘lang’ parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        about_page = AboutPage.objects.first()
        if not about_page:
            return Response({'detail': 'AboutPage not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutPageSerializer(about_page)

        data = {
            'section1_title': getattr(about_page, f'section1_title_{lang}', ''),
            'section1_subtitle': getattr(about_page, f'section1_subtitle_{lang}', ''),
            'section1_video': serializer.data['section1_video'],
            'section2_title': getattr(about_page, f'section2_title_{lang}', ''),
            'section2_description': getattr(about_page, f'section2_description_{lang}', ''),
            'section3_image': serializer.data['section3_image'],
            'section3_title': getattr(about_page, f'section3_title_{lang}', ''),
            'section3_description': getattr(about_page, f'section3_description_{lang}', ''),
            'section4_image': serializer.data['section4_image'],
            'section4_title': getattr(about_page, f'section4_title_{lang}', ''),
            'section4_description': getattr(about_page, f'section4_description_{lang}', ''),
            'section5_title': getattr(about_page, f'section5_title_{lang}', ''),
            'section5_description': getattr(about_page, f'section5_description_{lang}', ''),
            'team_members': serializer.data['team_members'],
            'section6_title': getattr(about_page, f'section6_title_{lang}', ''),
            'section6_banner': serializer.data['section6_banner'],
        }

        return Response(data, status=status.HTTP_200_OK)
