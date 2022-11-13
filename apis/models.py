from django.db import models




class Key(models.Model):
    key = models.CharField(max_length = 200, help_text='Enter any string to create or increment a key-value pair.', primary_key=True)
    value = models.IntegerField(default = 1, blank=True)

    def __str__(self):
        return f'{self.key} : {self.value}'
