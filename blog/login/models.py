from django.db import models

# Пользователь

class User(models.Model):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    balance = models.FloatField(default=0.0)
