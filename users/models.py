from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    stu_id = models.IntegerField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    member = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
