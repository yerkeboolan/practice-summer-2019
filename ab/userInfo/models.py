from django.db import models
from django.contrib.auth.models import User
from configuration.models import UserStatusConfig

# Create your models here.

class Teacher(models.Model):
    info = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.info.first_name + " " + self.info.last_name

class StudentManager(models.Manager):
    pass

class Student(models.Model):
    info = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(UserStatusConfig, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):
        return self.info.first_name + " " + self.info.last_name

    objects = StudentManager()

