from django.db import models

from blog.models import Blog


class BlogPage(models.Model):
    blog_page = models.ManyToManyField(Blog, related_name="blog_pages")

    def __str__(self):
        return f"Blog Page"