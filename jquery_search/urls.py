
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name='dashboard'),
    path(r'search/', views.get_city, name='search'),
    path(r'search_city_country/', views.get_city_country, name='search_city_country'),

]
