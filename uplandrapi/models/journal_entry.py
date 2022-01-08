from django.db import models

class JournalEntry(models.Model):
    title = models.CharField(max_length=50)
    entry_date = models.DateField()
    duration = models.TimeField()
    party = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    weather = models.CharField(max_length=50)
    # species = models.ForeignKey("Species", on_delete=models.CASCADE)
    gear = models.CharField(max_length=100)
    hunt_highlights = models.CharField(max_length=100)
    dogs = models.ManyToManyField("Dog", through="DogEntry", related_name="dogs")
    user = models.ForeignKey("JournalUser", on_delete=models.CASCADE)
    