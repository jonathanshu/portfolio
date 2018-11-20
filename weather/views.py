import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from weather import urls

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7ef4a6371824c7a7ad4b4e24ddbd11f8'

    if request.method == 'POST':
        form = CityForm(request.POST)
        print(request.POST.get('name'))
        # if :cit
        #     print(str(form.fields['name']) + "jksadkhadjkhasjkdhjkashd"
        # form.save()
    else:
        form = CityForm()

    cities = City.objects.all()
    #print(cities)
    weather_data = []

    for city in cities:
        urls.AddCity(city.name)
        r = requests.get(url.format(city)).json()
        # city.set_temp(r['main']['temp'])
        # city.set_desc(r['weather'][0]['description'])

        city_weather = {
            'city' : city.name,
            # 'temperature' : city.temperature,
            # 'description' : city.description,
            # 'icon' : r['weather'][0]['icon'],
            'id' : city.id
        }
        weather_data.append(city_weather)
        # print(city.name)
        #print(city_weather)

    context = {'weather_data' : weather_data,'form': form}



    form.save()

    return render(request, 'weather/weather.html', context)


# def city_index(request):
#     return render(request, 'weather/cities.html')

def city_detail(request, id):
    print(request)
    city = City.objects.get(id=id)
    print(id)
    context = {
        'city' : city.name,
        # 'temperature' : city.temperature,
        # 'description' : city.description,
        'id' : city.id
    }
    return render(request, 'weather/cities.html', context)
