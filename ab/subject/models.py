from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SubjectManager(models.Manager):
    pass

class Subject(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    # owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super(Subject, self).save(*args, **kwargs)
        subject_history = self.get_history_ent()
        subject_history.is_deleted = False
        subject_history.save()

    def delete(self, *args):
        subject_history = self.get_history_ent()
        subject_history.is_deleted = True
        subject_history.save()
        super(Subject, self).delete(*args)

    def get_history_ent(self):
        return SubjectHistory(
            title=self.title,
            created_date=self.created_date,
            origin_id=self.pk
        )

    def __str__(self):
        return "(" + str(self.pk) + ") " + self.title


    objects = SubjectManager()

class SubjectHistory(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner = models.IntegerField()
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class TopicManager(models.Manager):
    pass

class Topic(models.Model):
    title = models.CharField(max_length=255)
    is_quiz = models.BooleanField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="topic")
    # owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        super(Topic, self).save(*args, **kwargs)
        topic_history = self.get_history_ent()
        topic_history.is_deleted = False
        topic_history.save()


    def delete(self, *args):
        topic_history = self.get_history_ent()
        topic_history.is_deleted = True
        topic_history.save()
        super(Topic, self).delete(*args)



    def get_history_ent(self):
        return TopicHistory (
            title = self.title,
            is_quiz = self.is_quiz,
            subject_id = self.subject.pk,
            created_date = self.created_date,
            origin_id = self.pk
        )

    def __str__(self):
        return "(" + str(self.pk) + ") " + self.title

    class Meta:
        ordering = ['title', 'is_quiz']


    objects = TopicManager()

class TopicHistory(models.Model):
    title = models.CharField(max_length=255)
    is_quiz = models.BooleanField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner
    origin_id = models.IntegerField()
    subject_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SubtopicManager(models.Manager):
    pass


class SubtopicHistory(models.Model):
    title = models.CharField(max_length=255)
    topic_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Subtopic(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="subtopic")
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    # owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super(Subtopic, self).save(*args, **kwargs)
        subtopic_history = self.get_history_ent()
        subtopic_history.is_deleted = False
        subtopic_history.save()

    def delete(self, *args):
        subtopic_history = self.get_history_ent()
        subtopic_history.is_deleted = True
        subtopic_history.save()
        super(Subtopic, self).delete(*args)


    def get_history_ent(self):
        return SubtopicHistory (
            title = self.title,
            topic_id = self.topic.pk,
            created_date = self.created_date,
            origin_id = self.pk
        )


    def __str__(self):
        return "(" + str(self.pk) + ") " + self.title

    objects = SubtopicManager()