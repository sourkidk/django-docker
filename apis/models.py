from django.db import models
from django.db.models import JSONField





class Key(models.Model):
    key = models.CharField(max_length = 200, help_text='Enter any string to create or increment a key-value pair.', primary_key=True)
    value = models.IntegerField(default = 1, blank=True)

    def __str__(self):
        return f'{self.key} : {self.value}'

class Dog(models.Model):
    # original_json = models.CharField(max_length = 500)
    original_json = JSONField()
    # file_url = models.CharField(max_length = 500)


    def __str__(self):
        return self.original_json




