from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Blog 
from .models import BlogPage

@receiver(post_save, sender=Blog)
def create_blog_post_page(sender, instance, created, **kwargs):
    if created:
        blog_page, _ = BlogPage.objects.get_or_create() 
        blog_page.blog_page.add(instance)
