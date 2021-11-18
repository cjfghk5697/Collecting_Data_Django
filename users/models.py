from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.
class User(AbstractUser):
    stu_id=forms.IntegerField(label="Student ID",required=True) 
    name=forms.CharField(label="Name",required=True)
    email=forms.EmailField(label="E-mail",required=True)
    number=forms.IntegerField(label="Phone Number",required=True)