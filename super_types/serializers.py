from dataclasses import fields
from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'super_type']
        depth = 1