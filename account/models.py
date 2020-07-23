from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=35)
    email = models.EmailField()
    password = models.CharField(max_length=15)