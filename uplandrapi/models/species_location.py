from django.db import models

class SpeciesLocation(models.Model):
   species = models.ForeignKey("Species", on_delete=models.CASCADE)
   location = models.ForeignKey("Location", on_delete=models.CASCADE)