from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import HomePage
from .serializers import HomePageSerializer
from feedback.serializers import FeedbackSerializer
from frequently_questions.serializers import FrequentlyQuestionsSerializer
from our_services.serializers import OurServiceSerializer
from vehicles.serializers import VehicleSerializer

from drf_yasg.utils import swagger_auto_schema


class HomePageAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna o contéudo da tela Home passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.GET.get('lang')

        if not lang:
            return Response({'error': 'The “lang” parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        home_page = HomePage.objects.first()
        if not home_page:
            return Response({'detail': 'HomePage not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomePageSerializer(home_page)

        data = {
            'section1_banner': serializer.data['section1_banner'],
            'section1_title': getattr(home_page, f'section1_title_{lang}', ''),
            'section2_title': getattr(home_page, f'section2_title_{lang}', ''),
            'section2_image': serializer.data['section2_image'],
            'section2_services': OurServiceSerializer(home_page.section2_services.all(), many=True).data,
            'section3_title': getattr(home_page, f'section3_title_{lang}', ''),
            'section3_image': serializer.data['section3_image'],
            'differentials': serializer.data['differentials'],
            'section4_image': serializer.data['section4_image'],
            'section4_title': getattr(home_page, f'section4_title_{lang}', ''),
            'section4_description': getattr(home_page, f'section4_description_{lang}', ''),
            'section5_title': serializer.data['section5_title'],
            'section5_subtitle': getattr(home_page, f'section5_subtitle_{lang}', ''),
            'section5_feedbacks': FeedbackSerializer(home_page.section5_feedbacks.all(), many=True).data,
            'section6_title': getattr(home_page, f'section6_title_{lang}', ''),
            'section6_subtitle': getattr(home_page, f'section6_subtitle_{lang}', ''),
            'section6_vehicles': VehicleSerializer(home_page.section6_vehicles.all(), many=True).data,
            'section7_title': getattr(home_page, f'section7_title_{lang}', ''),
            'section7_frequently_questions': FrequentlyQuestionsSerializer(home_page.section7_frequently_questions.all(), many=True).data,
            'section8_title': getattr(home_page, f'section8_title_{lang}', ''),
            'section8_banner': serializer.data['section8_banner'],
        }

        return Response(data, status=status.HTTP_200_OK)
