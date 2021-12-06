from django.db import models

class DogEntry(models.Model):
   dog = models.ForeignKey("Dog", on_delete=models.CASCADE)
   entry = models.ForeignKey("JournalEntry", on_delete=models.CASCADE)