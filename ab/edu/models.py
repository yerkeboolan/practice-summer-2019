from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Teacher(models.Model):
    info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

class Student(models.Model):
    info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)


class Subject(models.Model):
    title = models.CharField(max_length=255)

class Group(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class GroupStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Topic(models.Model):
    title = models.CharField(max_length=255)
    is_quiz = models.BooleanField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Subtopic(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class Date(models.Model):
    date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Attendance(models.Model):
    att = models.BooleanField()
    rating = models.FloatField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)

class Video(models.Model):
    url = models.URLField()
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)

class VideoAccess(models.Model):
    access = models.BooleanField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)

class Test(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)

class TestAccess(models.Model):
    access = models.BooleanField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    flag = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)



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

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    def to_json(self):
        return {}
