from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=50)
   