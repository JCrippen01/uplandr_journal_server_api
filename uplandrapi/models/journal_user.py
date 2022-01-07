from django.db import models
from django.contrib.auth.models import User


class JournalUser(models.Model):
    """JournalUsers model"""
    bio = models.TextField(max_length=200)
    profile_img_url = models.ImageField()
    created_on = models.DateField(auto_now=True)
    # active = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)