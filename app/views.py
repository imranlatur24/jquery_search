from django.shortcuts import render
import json
from .models import CityModel,CityCountry
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    return render(request,'index.html')


def get_city(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = CityModel.objects.filter(city__icontains=q)
    results = []
    for pl in places:
      place_json = {}
      place_json = pl.city
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail in city'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def get_city_country(request):#get city as well as country data on city search pune-maharashtra
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = CityCountry.objects.filter(city__icontains=q)
    results = []
    for pl in places:
      place_json = {}
      place_json = pl.city + '-'+pl.country
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail in city country'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)