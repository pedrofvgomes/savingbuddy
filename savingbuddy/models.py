from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    activesince = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField(default=0)