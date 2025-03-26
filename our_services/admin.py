from django.contrib import admin
from .models import OurService
from .forms import OurServiceForm

class OurServiceAdmin(admin.ModelAdmin):
    form = OurServiceForm
    exclude = ['title', 'subtitle', 'description',]

admin.site.register(OurService, OurServiceAdmin)