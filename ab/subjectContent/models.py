from django.db import models
from subject.models import Subtopic

# Create your models here.

class Test(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', 'subtopic', ]

    def __str__(self):
        return self.subtopic.name

class Question(models.Model):
    question = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', 'question', ]

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    flag = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', 'answer', ]

    def __str__(self):
        return self.answer