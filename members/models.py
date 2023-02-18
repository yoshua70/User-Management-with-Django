from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DataBase(models.Model):
    label = models.CharField(max_length=100)


class Account(models.Model):
    email = models.CharField(max_length=100)
    db = models.ForeignKey(DataBase, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
