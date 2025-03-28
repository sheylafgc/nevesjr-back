from django.urls import path

from .views import *

app_name = 'frequently-questions'


urlpatterns = [
    path('frequently-questions', FrequentlyQuestionsListAPIView.as_view(), name='frequently-questions-list'),
    path('frequently-questions/<int:pk>', FrequentlyQuestionsDetailAPIView.as_view(), name='frequently-questions-detail'),
    path('frequently-questions/create', FrequentlyQuestionsCreateAPIView.as_view(), name='frequently-questions-create'),
    path('frequently-questions/update/<int:pk>', FrequentlyQuestionsUpdateAPIView.as_view(), name='frequently-questions-update'),
    path('frequently-questions/delete/<int:pk>', FrequentlyQuestionsDeleteAPIView.as_view(), name='frequently-questions-delete'),
]