from django.db import models
#from weather import urls

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)
    temperature = models.FloatField(max_length=10,null=False)
    description = models.CharField(max_length=100,null=False)
    # def __str__(self):
    #     self.temperature = 1
    #     print (self.temperature)
    #     #urls.AddCity(self.name)
    #     return self.name
    #
    # def set_temp(self, foo):
    #     # print(foo)
    #     self.temperature = foo
    #     # print(self.temperature)
    #     return
    # def set_desc(self, foo):
    #     # print(foo)
    #     self.description = foo
    #     return

    class Meta:
        verbose_name_plural = 'cities'
#
