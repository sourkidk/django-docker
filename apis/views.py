from django.shortcuts import render

# import viewsets
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, GenericAPIView

# import local data
from rest_framework.response import Response

from .serializers import KeySerializer
from .models import Key
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




