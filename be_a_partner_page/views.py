from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import BeAPartnerPage
from .serializers import BeAPartnerPageSerializer

from drf_yasg.utils import swagger_auto_schema


class BeAPartnerPageAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna o contéudo da tela Be a partner passando o idioma como parâmetro"
    )
    def get(self, request):
        lang = request.GET.get("lang")

        if not lang:
            return Response({"error": "The ‘lang’ parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        be_a_partner_page = BeAPartnerPage.objects.first()
        if not be_a_partner_page:
            return Response({"detail": "BeAPartnerPage not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BeAPartnerPageSerializer(be_a_partner_page)

        data = {
            "section1_banner": serializer.data["section1_banner"],
            "section1_banner_title": serializer.data.get(f"section1_banner_title_{lang}", ""),
            "section1_banner_description": serializer.data.get(f"section1_banner_description_{lang}", ""),
            "section1_form_title": serializer.data.get(f"section1_form_title_{lang}", ""),
            "section1_form_description": serializer.data.get(f"section1_form_description_{lang}", ""),
        }

        return Response(data, status=status.HTTP_200_OK)