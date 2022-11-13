from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
from re import search

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import KeySerializer, DogSerializer
from .models import Key, Dog
from django.db.models import F
from dog_list import helper





class KeyViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Key.objects.all()

    # specify serializer to be used
    serializer_class = KeySerializer


class IncrementKeyViewSet(UpdateAPIView):
    # define queryset
    queryset = Key.objects.all()

    # specify serializer to be used
    serializer_class = KeySerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        Key.objects.filter(pk=instance.key).update(value=F('value') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class DogViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Dog.objects.all()

    # specify serializer to be used
    serializer_class = DogSerializer

    def perform_create(self, serializer):

        # dog_api_call = requests.get('https://dog.ceo/api/breeds/image/random')
        # image_url = dog_api_call.json().get("message")
        # r = requests.get(image_url)
        #
        # print(search('breeds/', image_url))
        helper.download_images()

        file_name = f'test_image_file.jpg'

        # with open(file_name, 'wb') as f:
        #     f.write(r.content)
        serializer.save(original_json=file_name)






