from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import OurServicesPage
from .serializers import OurServicesPageSerializer

from drf_yasg.utils import swagger_auto_schema


class OurServicesPageAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna o contéudo da tela OurServices passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.GET.get('lang')

        if not lang:
            return Response({'error': 'The ‘lang’ parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        our_services_page = OurServicesPage.objects.first()
        if not our_services_page:
            return Response({'detail': 'OurServicesPage not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurServicesPageSerializer(our_services_page)

        response_data = {
            'section1_title': serializer.data['section1_title'],
            'section1_subtitle': serializer.data['section1_subtitle'],
            'section1_image': serializer.data['section1_image'],
            'section3_title': serializer.data['section3_title'],
            'section3_banner': serializer.data['section3_banner']
        }

        section2_services = serializer.data['section2_services']
        
        if section2_services:
            translated_services = []
            for service in section2_services:
                translated_services.append({
                    'id': service['id'],
                    'title': service.get(f'title_{lang}', service['title']),
                    'subtitle': service.get(f'subtitle_{lang}', service['subtitle']),
                    'description': service.get(f'description_{lang}', service['description']),
                    'image': service['image'],
                })
            response_data['section2_services'] = translated_services

        return Response(response_data, status=status.HTTP_200_OK)
