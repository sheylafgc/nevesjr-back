from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import activate

from .models import BlogPage
from .serializers import BlogPageSerializer

from drf_yasg.utils import swagger_auto_schema


class BlogPageAPIView(APIView):
    @swagger_auto_schema(
        operation_description='Retorna o contéudo da tela Blog passando o idioma como parâmetro'
    )
    def get(self, request):
        lang = request.GET.get('lang')

        if not lang:
            return Response({'error': 'The ‘lang’ parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        activate(lang)

        blog_page = BlogPage.objects.first()
        if not blog_page:
            return Response({'detail': 'BlogPage not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogPageSerializer(blog_page)

        translated_blogs = []
        for blog in serializer.data['blog_page']:
            translated_blogs.append({
                'id': blog['id'],
                'title': blog.get(f'title_{lang}', blog['title']),
                'subtitle': blog.get(f'subtitle_{lang}', blog['subtitle']),
                'description': blog.get(f'description_{lang}', blog['description']),
                'category': blog.get(f'category_{lang}', blog['category']),
                'image': blog['image'],
                'created_at': blog['created_at'],
            })

        return Response(translated_blogs, status=status.HTTP_200_OK)
