from django.db import models


# class GeeksModel(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.titleclass GeeksModel(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.title

class KeyValueModel(models.Model):
    key = models.CharField(max_length = 200)
    value = models.IntegerField(default = 1)

    def __str__(self):
        return f'{self.key} : {self.value}'
