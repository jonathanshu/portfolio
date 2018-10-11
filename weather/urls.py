from django.urls import path, include
from . import views
from weather import views

citylist = []

urlpatterns = [
    path('', views.index),
    path(r'^(?P<id>\d+)/$', views.city_detail)
]

#def get_city_name():
createdcities = []

# def AddCity(city_n):
#     for c in createdcities:
#         if c == city_n:
#             return
#     cityname = path(city_n+'/', views.city_index)
#     urlpatterns.append(cityname)
#     createdcities.append(city_n)
#     return
