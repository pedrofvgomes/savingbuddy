from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    balance = models.IntegerField(default=0)

class Log(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    value = models.IntegerField()
    remainingbalance = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
