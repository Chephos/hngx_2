from rest_framework import serializers

from . import models

class Person(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = ('id', 'name')
        read_only_fields = ('id',)
