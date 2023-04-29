from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
# Create your models here.
    
class CustomUser(AbstractUser):
    uid = models.CharField(max_length=8, default="")
    middle_name = models.CharField(max_length=255, null=True, blank=True, default="")
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')