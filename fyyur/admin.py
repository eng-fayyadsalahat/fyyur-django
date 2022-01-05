from django.contrib import admin
from . import models

# Register your models here.
myModels = [models.Venue, models.Artist, models.Show]
admin.site.register(myModels)
