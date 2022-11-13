from django.contrib import admin

# Register your models here.

from .models import Key, Dog


admin.site.register(Key)
admin.site.register(Dog)

