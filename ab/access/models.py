from django.db import models
from group.models import GroupStudent
from subjectContent.models import Test, Video

# Create your models here.



class VideoAccessManager(models.Manager):
    pass


class VideoAccess(models.Model):
    access = models.BooleanField()
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.PROTECT)


    objects = VideoAccessManager()


class TestAccessManager(models.Manager):
    pass


class TestAccess(models.Model):
    access = models.BooleanField()
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.PROTECT)

    objects = TestAccessManager()