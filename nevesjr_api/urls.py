"""nevesjr_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from payment.webhooks import stripe_webhook

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include('users.urls', namespace="users")),
    path('api/', include('our_services.urls', namespace="ourServices")),
    path('api/', include('vehicles.urls', namespace="vehicles")),
    path('api/', include('blog.urls', namespace="blog")),
    path('api/', include('contact.urls', namespace="contact")),
    path('api/', include('be_partner.urls', namespace="bePartner")),
    path('api/', include('frequently_questions.urls', namespace="frequentlQuestions")),
    path('api/', include('feedback.urls', namespace="feedback")),
    path('api/', include('payment.urls', namespace="payment")),
    path('api/', include('bookings.urls', namespace="bookings")),
    path('api/', include("forgot_password.urls", namespace="forgot-password")),
    path('api/content/', include("social_media.urls", namespace="social-media")),
    path('api/content/', include("contact_page.urls", namespace="contact-page")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
