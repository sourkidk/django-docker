
from rest_framework import serializers

# import model from models.py
from .models import Key




class KeySerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Key
        fields = ('key', 'value')
        # read_only_field = ('value',)


