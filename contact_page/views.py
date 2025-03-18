from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ContactPage
from .serializers import ContactPageSerializer

from django.utils.translation import activate


class ContactPageAPIView(APIView):
    def get(self, request):
        lang = request.GET.get("lang")

        if not lang:
            return Response({"error": "The ‘lang’ parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        contact_page = ContactPage.objects.first()
        if not contact_page:
            return Response({"detail": "ContactPage not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactPageSerializer(contact_page)

        data = {
            "id": serializer.data["id"],
            "section1_title": serializer.data.get(f"section1_title_{lang}", ""),
            "section1_description": serializer.data.get(f"section1_description_{lang}", ""),
            "section2_title": serializer.data.get(f"section2_title_{lang}", ""),
            "section1_banner": serializer.data["section1_banner"],
            "section2_banner": serializer.data["section2_banner"]
        }

        return Response(data, status=status.HTTP_200_OK)