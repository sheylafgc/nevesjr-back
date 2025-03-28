from django.contrib import admin
from .models import Blog
from .forms import BlogForm


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    exclude = ['title', 'subtitle', 'description', 'category',]

admin.site.register(Blog, BlogAdmin)