from django.db import models

# Create your models here.

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='display')