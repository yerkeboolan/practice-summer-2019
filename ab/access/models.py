from django.db import models
from subject.models import Subtopic
from group.models import GroupStudent
from subjectContent.models import Test

# Create your models here.

class Video(models.Model):
    url = models.URLField()
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

class VideoAccess(models.Model):
    access = models.BooleanField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)

class TestAccess(models.Model):
    access = models.BooleanField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)