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
    content = models.CharField(max_length=60)
    isComplete = models.BooleanField()
    createdAt = models.DateTimeField()
