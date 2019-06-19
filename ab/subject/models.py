from django.db import models

# Create your models here.


class SubjectManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Subject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "(" + str(self.pk) + ") " + self.title


    objects = SubjectManager()


class TopicManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Topic(models.Model):
    title = models.CharField(max_length=255)
    is_quiz = models.BooleanField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topic")


    def __str__(self):
        return "(" + str(self.pk) + ") " + self.title

    class Meta:
        ordering = ['title', 'is_quiz']


    objects = TopicManager()


class SubtopicManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Subtopic(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="subtopic")

    def __str__(self):
        return "(" + str(self.pk) + ") " + self.title

    objects = SubtopicManager()