from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog', BlogListAPIView.as_view(), name='blog-list'),
    path('blog/<int:pk>', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('blog/create', BlogCreateAPIView.as_view(), name='blog-create'),
    path('blog/update/<int:pk>', BlogUpdateAPIView.as_view(), name='blog-update'),
    path('blog/delete/<int:pk>', BlogDeleteAPIView.as_view(), name='blog-delete'),
    path('blog/categorie/<str:category>/', BlogCategoryListAPIView.as_view(), name='category-list'),
]