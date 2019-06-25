from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    info = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.info.first_name + " " + self.info.last_name

class Student(models.Model):
    info = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.info.first_name + " " + self.info.last_name