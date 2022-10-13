from io import open_code
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cars(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    number = models.IntegerField()
    def __str__(self):
        return self.model
class Drivers(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

