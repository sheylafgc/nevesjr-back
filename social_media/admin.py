from django.contrib import admin
from .models import SocialMedia
from .forms import SocialMediaForm

class SocialMediaAdmin(admin.ModelAdmin):
    form = SocialMediaForm
    exclude = ['label',]

admin.site.register(SocialMedia, SocialMediaAdmin)