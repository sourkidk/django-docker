from django.shortcuts import render

# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import KeyValueSerializer
# from .serializers import GeeksSerializer
from .models import KeyValueModel
# from .models import GeeksModel


# # create a viewset
# class GeeksViewSet(viewsets.ModelViewSet):
#     # define queryset
#     queryset = GeeksModel.objects.all()
#
#     # specify serializer to be used
#     serializer_class = GeeksSerializer

class KeyValueViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = KeyValueModel.objects.all()

    # specify serializer to be used
    serializer_class = KeyValueSerializer