from django.contrib import admin
from .models import Feedback
from .forms import FeedbackForm


class FeedbackAdmin(admin.ModelAdmin):
    form = FeedbackForm
    exclude = ['role', 'opinion',]

admin.site.register(Feedback, FeedbackAdmin)