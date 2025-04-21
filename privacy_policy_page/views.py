from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import PrivacyPolicyPage
from .serializers import PrivacyPolicyPageSerializer

from drf_yasg.utils import swagger_auto_schema


class PrivacyPolicyPageAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna o contéudo da tela Privacy Policy passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.GET.get('lang')

        if not lang:
            return Response({'error': 'The ‘lang’ parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        be_a_partner_page = PrivacyPolicyPage.objects.first()
        if not be_a_partner_page:
            return Response({'detail': 'PrivacyPolicyPage not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PrivacyPolicyPageSerializer(be_a_partner_page)

        data = {
            'content': serializer.data.get(f'content_{lang}', ''),
        }

        return Response(data, status=status.HTTP_200_OK)