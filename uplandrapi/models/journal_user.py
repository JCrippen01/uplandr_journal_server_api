from django.db import models
from django.contrib.auth.models import User


class JournalUser(models.Model):
    """JournalUsers model"""
    created_on = models.DateField(auto_now=True)
    # active = models.BooleanField()
    user = models.OneToOneField(User, null =True, on_delete=models.CASCADE)