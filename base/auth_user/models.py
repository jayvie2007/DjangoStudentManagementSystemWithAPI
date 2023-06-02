from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
import random
# Create your models here.
    
class CustomUser(AbstractUser):

    uid = models.CharField(max_length=8, default="")
    middle_name = models.CharField(max_length=255, null=True, blank=True, default="")
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')
    
    def __str__(self):
        return self.username + " " + self.email


class UserData(models.Model):
    gender_choices = (
    ('Male', "Male"),
    ('Female', "Female"),
    ('Other', "Other"),
)
    student_number = models.CharField(max_length=8, default="")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=gender_choices,max_length=20, default="")
    year = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)

    # def save(self):
    #     self.student_number = str(random.randint(10000000, 99999999))
    #     super(UserData, self).save()

    def __str__(self):
        return self.first_name + " " + self.last_name
    

