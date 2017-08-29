from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField("username",max_length=100,unique=True,db_index=True)
    email = models.EmailField("email_address",unique=True)
    password = models.CharField("password",max_length=20)
    joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELF = "username"


    def __str__(self):
        return self.username