from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from re import search


# import viewsets
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, GenericAPIView

# import local data
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



# class DogViewSet(viewsets.ViewSet):
#     # define queryset
#     queryset = Dog.objects.all()
#
#     # specify serializer to be used
#     serializer_class = DogSerializer
#
#     def create(self, request):
#         queryset = Dog.objects.all()
#
#         # pull data from third party rest api
#         response = requests.get('https://dog.ceo/api/breeds/image/random')
#         # convert reponse data into json
#         # print(response)
#         dog_fetch = response.json()
#         print(dog_fetch)
#
#         # return HttpResponse(response)
#         serializer = DogSerializer(queryset, many=True)
#         # serializer = DogSerializer(dog_fetch)
#
#         return Response(serializer.data)
#         # return Dog.objects.create('test')
#         # return Dog.objects.create(response)
#
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def list(self, request):
#         queryset = Dog.objects.all()
#         serializer = DogSerializer(queryset, many=True)
#         return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
    #     return render(request, 'books/book-create.html', {'form': form})








