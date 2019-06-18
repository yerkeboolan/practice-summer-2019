from django.db import models
from group.models import GroupStudent, Group
from userInfo.models import Student
from subject.models import Topic, Subject

# Create your models here.


class Date(models.Model):
    date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Attendance(models.Model):
    att = models.BooleanField()
    rating = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)


class QuizRating(models.Model):
    date = models.DateField()
    theory = models.IntegerField()
    practice = models.IntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class RealTest(models.Model):
    date = models.DateField()
    score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

# class TestResult(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)