from django.db import models

# Create your models here.

class Contect(models.Model):
    name = models.CharField(max_length=35)
    email= models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()
    