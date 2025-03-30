from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class AboutPage(models.Model):
    section1_title = models.TextField(blank=True, null=True)
    section1_subtitle = models.TextField(blank=True, null=True)
    section1_video = models.FileField(upload_to='about_page/section1/video', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    section2_title = models.TextField(blank=True, null=True)
    section2_description = models.TextField(blank=True, null=True)
    section3_image = models.ImageField(upload_to='about_page/section3/image', blank=True, null=True,)
    section3_title = models.TextField(blank=True, null=True)
    section3_description = models.TextField(blank=True, null=True)
    section4_image = models.ImageField(upload_to='about_page/section4/image', blank=True, null=True,)
    section4_title = models.TextField(blank=True, null=True)
    section4_description = models.TextField(blank=True, null=True)
    section5_title = models.TextField(blank=True, null=True)
    section5_description = models.TextField(blank=True, null=True)
    section6_title = models.TextField(blank=True, null=True)
    section6_banner = models.ImageField(upload_to='about_page/section6/banner', blank=True, null=True)

    def save(self, *args, **kwargs):
        if AboutPage.objects.exists() and not self.pk:
            raise ValidationError('Only one AboutPage registration is allowed.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'About Page'

class TeamMember(models.Model):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='about_page/section5/team_avatars', blank=True, null=True)

    def __str__(self):
        return self.name