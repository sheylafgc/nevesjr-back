import re
import unicodedata
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Blog
from .serializers import BlogSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BlogListAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna todos os post blogs"
    )
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
class BlogCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Cria um post blog",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description="Título do post blog"),
                'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description="Subtítulo do post blog"),
                'image': openapi.Schema(type=openapi.TYPE_FILE, description="Imagem do post blog"),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description="Descrição do post blog"),
                'category': openapi.Schema(type=openapi.TYPE_STRING, description="Categoria do post blog"),
            },
        ),
        responses={
            201: "",
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retorna um post blog"
    )
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
class BlogUpdateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Atualiza um post blog",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description="Título do post blog"),
                'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description="Subtítulo do post blog"),
                'image': openapi.Schema(type=openapi.TYPE_FILE, description="Imagem do post blog"),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description="Descrição do post blog"),
                'created_at': openapi.Schema(type=openapi.TYPE_STRING, description="Data de criação do post blog"),
                'category': openapi.Schema(type=openapi.TYPE_STRING, description="Categoria do post blog"),
            },
        ),
        responses={
            200: "",
        }, 
    )
    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDeleteAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Deleta um post blog"
    )
    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogCategoryListAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Lista todas as categorias do blog",
    )
    def get(self, request):
        categories = (
            Blog.objects.exclude(category__isnull=True)
            .exclude(category="")
            .values_list("category", flat=True)
            .distinct()
        )

        def clean_value(category):
            category = "".join(
                c for c in unicodedata.normalize("NFD", category) if unicodedata.category(c) != "Mn"
            )

            category = re.sub(r"[^a-zA-Z0-9]", "", category)
            return category.lower()

        formatted_categories = [{"label": category, "value": clean_value(category)} for category in categories]

        return Response(formatted_categories, status=status.HTTP_200_OK)
    
class BlogByCategoryAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Lista os post blogs por categoria",
    )
    def get(self, request, category):
        blogs = Blog.objects.filter(category=category)
        
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)