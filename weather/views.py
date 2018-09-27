import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from weather import urls

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7ef4a6371824c7a7ad4b4e24ddbd11f8'
    city = 'Boston'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        urls.AddCity(city.name)
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        print(city_weather)

    context = {'weather_data' : weather_data,'form': form}

    return render(request, 'weather/weather.html', context)

def city_index(request):
    return render(request, 'weather/cities.html')
