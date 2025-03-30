from django.db import models


class FrequentlyQuestions(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question if self.question else 'Untitled FrequentlyQuestions'