from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField()
    date = models.DateField()
    