from django.contrib import admin
from django.db.models.fields import CharField
from .models import CityModel,CityCountry
# Register your models here.
admin.site.register(CityModel)
admin.site.register(CityCountry)