from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import HomePage
from our_services.models import OurService
from feedback.models import Feedback
from vehicles.models import Vehicle
from frequently_questions.models import FrequentlyQuestions

@receiver(post_save, sender=HomePage)
def create_home_page_relations(sender, instance, created, **kwargs):
    if created:
        instance.section2_services.add(*OurService.objects.all())
        instance.section5_feedbacks.add(*Feedback.objects.all())
        instance.section6_vehicles.add(*Vehicle.objects.all()) 
        instance.section7_frequently_questions.add(*FrequentlyQuestions.objects.all())
