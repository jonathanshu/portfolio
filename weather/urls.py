from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    # path(views.city, views.city_index)
]

#def get_city_name():


def AddCity(city_n):
    cityname = path(city_n+'/', views.city_index)
    urlpatterns.append(cityname)
    print('got here')
    return
