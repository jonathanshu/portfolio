from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        # 'temperature' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Temperature'}),
        # 'description' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Description'})
        }
