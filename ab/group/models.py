from django.db import models
from userInfo.models import Teacher, Student
from subject.models import Subject


# Create your models here.

class GroupManager(models.Manager):
    pass

class Group(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    objects = GroupManager()


class GroupStudentManager(models.Manager):
        pass

class GroupStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    objects = GroupStudentManager()