from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
# Create your models here.

class AccountModel(models.Model):
    uid = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    