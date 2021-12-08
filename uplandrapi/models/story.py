from django.db import models

class Story(models.Model):
    user = models.ForeignKey("JournalUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    entry_date = models.DateField()
    image_url = models.URLField()
    content = models.CharField(max_length=500)
    