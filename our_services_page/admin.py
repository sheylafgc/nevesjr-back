from django.contrib import admin
from .models import OurServicesPage
from .forms import OurServicesPageForm

class OurServicesPageAdmin(admin.ModelAdmin):
    form = OurServicesPageForm
    exclude = ['section1_title', 'section1_subtitle', 'section3_title',]

admin.site.register(OurServicesPage, OurServicesPageAdmin)