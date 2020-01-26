from rest_framework import serializers

from .models import Hero, Task


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('giver', 'map', 'content', 'isComplete',
                  'createdAt', 'lastModified')
