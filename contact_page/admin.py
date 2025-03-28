from django.contrib import admin
from .models import ContactPage
from .forms import ContactPageForm


class ContactPageAdmin(admin.ModelAdmin):
    form = ContactPageForm
    exclude = ['section1_form_title', 'section1_form_description', 'section2_banner_title',]

admin.site.register(ContactPage, ContactPageAdmin)