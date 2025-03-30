from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import HomePage


def add_differentials_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.differentials.add(instance)

def add_our_services_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section2_services.add(instance)

def add_feedbacks_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section5_feedbacks.add(instance)

def add_vehicles_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section6_vehicles.add(instance)

def add_frequently_question_to_homepage(sender, instance, created, **kwargs):
    if created:
        homepage, _ = HomePage.objects.get_or_create()
        homepage.section7_frequently_questions.add(instance)