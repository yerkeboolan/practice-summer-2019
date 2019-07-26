from django.db import models
from subject.models import Subtopic

# Create your models here.

class VideoManager(models.Manager):
    pass

class Video(models.Model):
    url = models.URLField()
    subtopic = models.ForeignKey(Subtopic, on_delete=models.PROTECT)

    def __str__(self):
        return self.url

    objects = VideoManager()

class TestManager(models.Manager):
    pass

class Test(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.PROTECT)

    class Meta:
        ordering = ['id', 'subtopic', ]

    def __str__(self):
        return self.subtopic.title

    objects = TestManager()

class QuestionManager(models.Manager):
    pass

class Question(models.Model):
    question = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, related_name="q_test")

    class Meta:
        ordering = ['id', 'question', ]

    def __str__(self):
        return self.question

    objects = QuestionManager()

class AnswerManager(models.Manager):
    pass

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    flag = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="ans_question")

    class Meta:
        ordering = ['id', 'answer', ]

    def __str__(self):
        return self.answer

    objects = AnswerManager()