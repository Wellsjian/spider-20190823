from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Publiser)
admin.site.register(models.Book2)