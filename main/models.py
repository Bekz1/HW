from django.db import models

# Create your models here.

class Cars(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    number = models.IntegerField()
    def __str__(self):
        return self.model
class Drivers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car = models.ManyToManyField(Cars)
    def __str__(self):
        return self.first_name