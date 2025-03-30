from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import HomePage, HomePageDifferentials
from our_services.models import OurService
from feedback.models import Feedback
from vehicles.models import Vehicle
from frequently_questions.models import FrequentlyQuestions


@receiver(post_save, sender=HomePageDifferentials)
def add_differentials_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.differentials.add(instance)

@receiver(post_save, sender=OurService)
def add_our_services_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section2_services.add(instance)

@receiver(post_save, sender=Feedback)
def add_feedbacks_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section5_feedbacks.add(instance)

@receiver(post_save, sender=Vehicle)
def add_vehicles_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section6_vehicles.add(instance)

@receiver(post_save, sender=FrequentlyQuestions)
def add_frequently_question_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section7_frequently_questions.add(instance)