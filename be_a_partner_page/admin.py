from django.contrib import admin
from .models import BeAPartnerPage
from .forms import BeAPartnerPageForm

class BeAPartnerPageAdmin(admin.ModelAdmin):
    form = BeAPartnerPageForm
    exclude = ['section1_banner_title', 'section1_banner_description', 'section1_form_title', 'section1_form_description',]

admin.site.register(BeAPartnerPage, BeAPartnerPageAdmin)