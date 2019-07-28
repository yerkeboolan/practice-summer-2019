from django.db import models
from subject.models import Subtopic

# Create your models here.

class VideoManager(models.Manager):
    pass

class Video(models.Model):
    url = models.URLField()
    subtopic = models.ForeignKey(Subtopic, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.url

    objects = VideoManager()


    def get_history_ent(self):
        return VideoHistory(
            url = self.url,
            subtopic_id = self.subtopic.pk,
            created_date = self.created_date,
            origin_id = self.pk
        )


    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)
        video_history = self.get_history_ent()
        video_history.is_deleted = False
        video_history.save()


    def delete(self, *args):
        video_history = self.get_history_ent()
        video_history.is_deleted = True
        video_history.save()
        super(Video, self).delete(*args)



class VideoHistory(models.Model):
    url = models.URLField()
    subtopic_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.url

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