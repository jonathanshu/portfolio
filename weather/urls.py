from django.urls import path, include
from . import views
from weather import views

urlpatterns = [
    path('', views.index),
    # path(views.city, views.city_index)
]

#def get_city_name():


def AddCity(city_n):
    if (len(urlpatterns)+1) == len(views.citylist):
        print ("cities already created")
        return
    print(len(urlpatterns)+1)
    print(len(views.citylist))
    cityname = path(city_n+'/', views.city_index)
    urlpatterns.append(cityname)
    return
