from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    info = models.ForeignKey(User, on_delete=models.CASCADE)

class Student(models.Model):
    info = models.ForeignKey(User, on_delete=models.CASCADE)