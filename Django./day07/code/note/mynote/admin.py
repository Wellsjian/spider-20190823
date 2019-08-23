from django.contrib import admin
from . import models
from user import models as u_models

# Register your models here.
admin.site.register(u_models.User)
admin.site.register(models.Note)
