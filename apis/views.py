from django.shortcuts import render
from django.http import HttpResponse
import requests


# import viewsets
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, GenericAPIView

# import local data
from rest_framework.response import Response

from .serializers import KeySerializer, DogSerializer
from .models import Key, Dog
from django.db.models import F




class KeyViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Key.objects.all()

    # specify serializer to be used
    serializer_class = KeySerializer


# class CreateKeyViewSet(CreateAPIView):
#     # define queryset
#     queryset = Key.objects.all()
#
#     # specify serializer to be used
#     serializer_class = KeySerializer

# class UpdateKeyViewSet(UpdateAPIView):
#     # define queryset
#     queryset = Key.objects.all()
#
#     # specify serializer to be used
#     serializer_class = KeySerializer

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

# class DogViewSet(viewsets.ModelViewSet):
#     # define queryset
#     queryset = Dog.objects.all()
#
#     # specify serializer to be used
#     serializer_class = DogSerializer
#
#     def users(request):
#         # pull data from third party rest api
#         response = requests.get('https://jsonplaceholder.typicode.com/users')
#         # convert reponse data into json
#         users = response.json()
#         print(users)
#         return HttpResponse("Users")
#         pass

class DogViewSet(viewsets.ViewSet):
    # define queryset
    queryset = Dog.objects.all()

    # specify serializer to be used
    serializer_class = DogSerializer

    def create(self, request):
        queryset = Dog.objects.all()

        # pull data from third party rest api
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        # convert reponse data into json
        users = response.json()
        print(users)
        # return HttpResponse(response)
        serializer = DogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pass

    def list(self, request):
        queryset = Dog.objects.all()
        serializer = DogSerializer(queryset, many=True)
        return Response(serializer.data)









