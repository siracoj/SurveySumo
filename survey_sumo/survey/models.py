from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.db.models.aggregates import Count
from random import randint


class Question(models.Model):
    """
    Model to hold all questions to be answered by users
    """
    question = models.CharField(max_length=1000)
    choices = JSONField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    """
    Model to hold users answers
    Contains which user answered, what question they answered, and the answer itself
    """

    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.answer




