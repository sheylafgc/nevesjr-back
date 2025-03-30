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

        response_data = {}

        response_data['section1_banner'] = serializer.data['section1_banner']
        response_data['section1_title'] = getattr(home_page, f'section1_title_{lang}', '')
        response_data['section2_title'] = getattr(home_page, f'section2_title_{lang}', '')
        response_data['section2_image'] = serializer.data['section2_image']
        
        section2_services = serializer.data.get('section2_services', [])
        if section2_services:
            translated_services = []
            for service in section2_services:
                translated_services.append({
                    'id': service['id'],
                    'title': service.get(f'title_{lang}', service['title']),
                    'subtitle': service.get(f'subtitle_{lang}', service['subtitle']),
                    'image': service['image'],
                })
            response_data['section2_services'] = translated_services

        response_data['section3_title'] = getattr(home_page, f'section3_title_{lang}', '')
        response_data['section3_image'] = serializer.data['section3_image']

        differentials = serializer.data.get('differentials', [])
        if differentials:
            translated_differentials = []
            for differential in differentials:
                translated_differentials.append({
                    'id': differential['id'],
                    'title': differential.get(f'title_{lang}', differential['title']),
                    'description': differential.get(f'description_{lang}', differential['description']),
                })
                response_data['differentials'] = translated_differentials
        
        response_data['section4_image'] = serializer.data['section4_image']
        response_data['section4_title'] = getattr(home_page, f'section4_title_{lang}', '')
        response_data['section4_description'] = getattr(home_page, f'section4_description_{lang}', '')

        response_data['section5_title'] = getattr(home_page, f'section5_title_{lang}', '')
        response_data['section5_subtitle'] = getattr(home_page, f'section5_subtitle_{lang}', '')

        section5_feedbacks = serializer.data.get('section5_feedbacks', [])
        if section5_feedbacks:
            translated_feedbacks = []
            for feedback in section5_feedbacks:
                translated_feedbacks.append({
                    'id': feedback['id'],
                    'name': feedback['name'],
                    'role': feedback.get(f'role_{lang}', feedback['role']),
                    'opinion': feedback.get(f'opinion_{lang}', feedback['opinion']),
                    'user_image': feedback['user_image'],
                })
            response_data['section5_feedbacks'] = translated_feedbacks

        response_data['section6_title'] = getattr(home_page, f'section6_title_{lang}', '')
        response_data['section6_subtitle'] = getattr(home_page, f'section6_subtitle_{lang}', '')

        section6_vehicles = serializer.data.get('section6_vehicles', [])
        if section6_vehicles:
            translated_vehicles = []
            for vehicle in section6_vehicles:
                translated_vehicles.append({
                    'id': vehicle['id'],
                    'car_image': vehicle['car_image'],
                    'car_name': vehicle.get(f'car_name_{lang}', vehicle['car_name']),
                    'car_type': vehicle.get(f'car_type_{lang}', vehicle['car_type']),
                    'quantity_luggage': vehicle['quantity_luggage'],
                    'quantity_seats': vehicle['quantity_seats'],
                })
            response_data['section6_vehicles'] = translated_vehicles

        response_data['section7_title'] = getattr(home_page, f'section7_title_{lang}', '')

        section7_frequently_questions = serializer.data.get('section7_frequently_questions', [])
        if section7_frequently_questions:
            translated_frequently_questions = []
            for frequently_questions in section7_frequently_questions:
                translated_frequently_questions.append({
                    'id': frequently_questions['id'],
                    'question': frequently_questions.get(f'question_{lang}', frequently_questions['question']),
                    'answer': frequently_questions.get(f'answer_{lang}', frequently_questions['answer']),
                })
            response_data['section7_frequently_questions'] = translated_frequently_questions

        response_data['section8_title'] = getattr(home_page, f'section8_title_{lang}', '')
        response_data['section8_banner'] = serializer.data['section8_banner']

        return Response(response_data, status=status.HTTP_200_OK)
