from django.db import models
#from weather import urls

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        #urls.AddCity(self.name)
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
