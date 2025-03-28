from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import OurFleetPage
from .serializers import OurFleetPageSerializer

from drf_yasg.utils import swagger_auto_schema


class OurFleetPageAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna o contéudo da tela OurFleet passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.GET.get('lang')

        if not lang:
            return Response({'error': 'The ‘lang’ parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        our_fleet_page = OurFleetPage.objects.first()
        if not our_fleet_page:
            return Response({'detail': 'OurFleetPage not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurFleetPageSerializer(our_fleet_page)

        response_data = {
            'section1_title': serializer.data['section1_title'],
            'section1_subtitle': serializer.data['section1_subtitle'],
            'section1_banner': serializer.data['section1_banner'],
        }

        section2_vehicles = serializer.data['section2_vehicles']
        
        if section2_vehicles:
            translated_fleet = []
            for service in section2_vehicles:
                translated_fleet.append({
                    'id': service['id'],
                    'car_name': service.get(f'car_name_{lang}', service['car_name']),
                    'car_type': service.get(f'car_type_{lang}', service['car_type']),
                    'car_overview': service.get(f'car_overview_{lang}', service['car_overview']),
                    'car_amenities': service.get(f'car_amenities_{lang}', service['car_amenities']),
                    'car_best_for_services': service.get(f'car_best_for_services_{lang}', service['car_best_for_services']),
                    'car_image': service['car_image'],
                    'quantity_seats': service['quantity_seats'],
                    'quantity_luggage': service['quantity_luggage'],
                    'price_km': service['price_km'],
                    'price_hour': service['price_hour'],
                })
            response_data['section2_vehicles'] = translated_fleet

        return Response(response_data, status=status.HTTP_200_OK)
