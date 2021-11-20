from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    stu_id = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(null=True)
    member = models.BooleanField(null=True, default=False)
