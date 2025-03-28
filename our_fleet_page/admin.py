from django.contrib import admin
from .models import OurFleetPage
from .forms import OurFleetPageForm


class OurFleetPageAdmin(admin.ModelAdmin):
    form = OurFleetPageForm
    exclude = ['section1_title', 'section1_subtitle',]

admin.site.register(OurFleetPage, OurFleetPageAdmin)