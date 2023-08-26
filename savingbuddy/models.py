from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Account(models.Model):
    balance = models.IntegerField(default=0)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class Log(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    value = models.IntegerField()
    remainingbalance = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)
