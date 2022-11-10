# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import KeyValueModel
# from .models import GeeksModel


# # Create a model serializer
# class GeeksSerializer(serializers.HyperlinkedModelSerializer):
#     # specify model and fields
#     class Meta:
#         model = GeeksModel
#         fields = ('title', 'description')

class KeyValueSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = KeyValueModel
        fields = ('key', 'value')