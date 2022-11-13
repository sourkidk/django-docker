from django.test import TestCase, Client
from rest_framework import status

from .models import Key
from .serializers import KeySerializer

""" Test module for Key model """

client = Client()

class GetKeyTest(TestCase):
    def setUp(self):
        Key.objects.create(key='Walk the Earth')


    def test_key_value(self):
        key_walk_the_earth = Key.objects.get(key='Walk the Earth')
        self.assertEqual(key_walk_the_earth.value, 1)

class GetAllKeysTest(TestCase):
    def setUp(self):
        Key.objects.create(key='Walk the Earth')
        Key.objects.create(key='Tallest Man on Earth')
        Key.objects.create(key='Earthlings')
        Key.objects.create(key='Earth is for lovers')


    def test_get_all_key_value(self):
        # get API response
        response = client.get('/key/')
        # get data from db
        keys = Key.objects.all()
        serializer = KeySerializer(keys, many=True)
        self.assertEqual(response.data, serializer.data)
        # print(f'serializer: {serializer.data}')
        # print(f'response: {response.data}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)






