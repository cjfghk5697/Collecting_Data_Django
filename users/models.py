from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    stu_id = models.IntegerField(blank=True, default=False)
    member = models.BooleanField(default=False)
    email = models.EmailField(blank=True, default=False)
