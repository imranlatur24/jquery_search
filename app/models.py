from django.db import models

# Create your models here.
class CityModel(models.Model):
    city=models.CharField(max_length=25)
    class Meta:
        db_table='search_city'
    def __str__(self) -> str:
        return self.city

class CityCountry(models.Model):
    city=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    class Meta:
        db_table='search_city_country'
    def __str__(self) -> str:
        return self.city and self.country