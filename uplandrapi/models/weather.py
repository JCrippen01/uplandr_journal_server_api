from django.db import models

class Weather(models.Model):
    date = models.DateField()
    temperature = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_direction = models.IntegerField()
    conditions = models.ManyToManyField("Dog", through="DogEntry", related_name="dogs")
    moon_phase = models.CharField(max_length=100)
    hunt_highlights = models.CharField(max_length=100)
    barometric_pressure = models.IntegerField()
    