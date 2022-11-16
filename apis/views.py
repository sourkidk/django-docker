
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import KeySerializer, DogSerializer
from .models import Key, Dog
from django.db.models import F
from dog_list import helper

# Main Key viewset covers most CRUD functionality besides incrementing the value
class KeyViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Key.objects.all()

    # specify serializer to be used
    serializer_class = KeySerializer

# Added an additional view to accomodate the need to increment the values.
class IncrementKeyViewSet(UpdateAPIView):
    # define queryset
    queryset = Key.objects.all()

    # specify serializer to be used
    serializer_class = KeySerializer

    # Define patch functionality to increment value of a given key
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

    # Override create for viewset
    def perform_create(self, serializer):

        # Get an image from dog.ceo, save it, modify it and extract metadata.
        json_message, file_name, mod_file_name, metadata = helper.download_images()

        # Populate database fields for each Dog image
        serializer.save(original_json=json_message, image=file_name, modified_image=mod_file_name, metadata=metadata)




