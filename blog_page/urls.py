from django.urls import path

from .views import *

app_name = 'blog_page'


urlpatterns = [
    path('blog-page/', BlogPageAPIView.as_view(), name='blog-page'),
    path('blog-page-carousel/', BlogPageAPIView.as_view(), name='blog-page-carousel'),
]