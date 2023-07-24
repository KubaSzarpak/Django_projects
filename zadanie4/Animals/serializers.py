from rest_framework import serializers
from Animals.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'description', 'category', 'area']
