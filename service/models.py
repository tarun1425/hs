from django.db import models

# Create your models here.

class Have_Flat(models.Model):
    location = models.CharField(max_length=75)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    rent = models.FloatField()
    email = models.EmailField()
    
class Need_Flat(models.Model):
    location_1 = models.CharField(max_length=75)
    location_2 = models.CharField(max_length=75)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    rent = models.FloatField()
    email = models.EmailField()