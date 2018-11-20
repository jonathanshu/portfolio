from django.urls import path, include
from . import views
from weather import views
from .models import City

citylist = []

urlpatterns = [
    path('', views.index),
    #path('<slug:name>', views.city_detail)
    path('<int:id>', views.city_detail, name='details')
]

#def get_city_name():
createdcities = []

# def AddCity(city_n):
#     for c in createdcities:
#         if c == city_n:
#             return
#     # cityname = path(city_n+'/', views.city_detail, name=city_n)
#     cityname = path(city_n+'/', views.city_detail)
#     urlpatterns.append(cityname)
#     createdcities.append(city_n)
#     return

def AddCity(city_n):
    for c in createdcities:
        if c == city_n:
            return
    # cityname = path(city_n+'/', views.city_detail, name=city_n)
    cityname = path(city_n+'/', views.city_detail)
    urlpatterns.append(cityname)
    createdcities.append(city_n)
    return
