from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=200)