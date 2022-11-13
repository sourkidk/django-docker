
from rest_framework import serializers

# import model from models.py
from .models import Key, Dog




class KeySerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Key
        fields = ('key', 'value')
        # read_only_field = ('value',)

class DogSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Dog
        # fields = ('original_json', 'file_url')
        fields = ('original_json',)
        fields = ('original_json',)


