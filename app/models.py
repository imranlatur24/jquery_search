from django.db import models

# Create your models here.
class CityModel(models.Model):
    city=models.CharField(max_length=25)
    class Meta:
        db_table='search_city'

class CityCountry(models.Model):
    city=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    class Meta:
        db_table='search_city_country'