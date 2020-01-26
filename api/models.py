"""importing models"""
from django.db import models

# Create your models here.


class Hero(models.Model):
    """Hero model"""
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Task(models.Model):
    """Task model"""
    class Giver(models.TextChoices):
        PRAPOR = 'prapor'
        THERAPIST = 'therapist'
        SKIER = 'skier'
        PEACEKEEPER = 'peacekeeper'
        MECHANIC = 'mechanic'
        RAGMAN = 'ragman'
        JAEGER = 'jaeger'
        FENCE = 'fence'

    class Map(models.TextChoices):
        CUSTOMS = 'customs'
        FACTORY = 'factory'
        WOODS = 'woods'
        INTERCHANGE = 'interchange'
        RESERVE = 'reserve'
        SHORELINE = 'shoreline'
        LABS = 'labs'

    giver = models.TextField(default=Giver.PRAPOR, choices=Giver.choices)
    map = models.TextField(default=Map.CUSTOMS, choices=Map.choices)
    content = models.CharField(max_length=60)
    isComplete = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
