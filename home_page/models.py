from django.db import models
from django.core.exceptions import ValidationError

from our_services.models import OurService
from feedback.models import Feedback
from vehicles.models import Vehicle
from frequently_questions.models import FrequentlyQuestions


class HomePage(models.Model):
    section1_banner = models.ImageField(upload_to='home_page/section1/banner', blank=True, null=True)
    section1_title = models.TextField(blank=True, null=True)
    section2_title = models.TextField(blank=True, null=True)
    section2_image = models.ImageField(upload_to='home_page/section2/image', blank=True, null=True)
    section2_services = models.ManyToManyField(OurService, related_name='home_page_services', blank=True, null=True)
    section2_description = models.TextField(blank=True, null=True)
    section3_title = models.TextField(blank=True, null=True)
    section3_image = models.ImageField(upload_to='home_page/section3/image', blank=True, null=True)
    section4_image = models.ImageField(upload_to='home_page/section4/image', blank=True, null=True)
    section4_title = models.TextField(blank=True, null=True)
    section4_description = models.TextField(blank=True, null=True)
    section5_title = models.TextField(blank=True, null=True)
    section5_subtitle = models.TextField(blank=True, null=True)
    section5_feedbacks = models.ManyToManyField(Feedback, related_name='home_page_feedbacks', blank=True, null=True)
    section6_title = models.TextField(blank=True, null=True)
    section6_subtitle = models.TextField(blank=True, null=True)
    section6_vehicles = models.ManyToManyField(Vehicle, related_name='home_page_vehicles', blank=True, null=True)
    section7_title = models.TextField(blank=True, null=True)
    section7_frequently_questions = models.ManyToManyField(FrequentlyQuestions, related_name='home_page_frequently_questions', blank=True, null=True)
    section8_title = models.TextField(blank=True, null=True)
    section8_banner = models.ImageField(upload_to='home_page/section8/banner', blank=True, null=True)

    def save(self, *args, **kwargs):
        if HomePage.objects.exists() and not self.pk:
            raise ValidationError('Only one HomePage registration is allowed.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Home Page'

class HomePageDifferentials(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='differentials')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.homepage.differentials.count() >= 4 and not self.pk:
            raise ValidationError('Only 4 differentials can be added per HomePage.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title