from django.db import models

# Create your models here.
class AccountModel(models.Model):
    uid = models.CharField(max_length=8)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    