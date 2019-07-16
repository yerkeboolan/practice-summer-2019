from django.db import models
from group.models import GroupStudent, Group
from userInfo.models import Student
from subject.models import Topic, Subject

# Create your models here.


class GroupAttendance(models.Model):
    date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class StudentAttendance(models.Model):
    att = models.BooleanField()
    rating = models.FloatField()
    date = models.ForeignKey(GroupAttendance, on_delete=models.CASCADE)
    group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)


class QuizRatingManager(models.Manager):
    pass

class QuizRating(models.Model):
    date = models.DateField()
    theory = models.IntegerField()
    practice = models.IntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now = True, auto_now_add=False)
    # owner



    def get_history_ent(self):
        return QuizHistory(
            date = self.date,
            theory = self.theory,
            practice = self.practice,
            topic_id = self.topic.pk,
            student_id = self.student.pk,
            origin_id = self.pk,
            created_date = self.created_date,
        )


    def save(self, *args, **kwargs):
        super(QuizRating, self).save(*args, **kwargs)
        quiz_history = self.get_history_ent()
        quiz_history.is_deleted = False
        quiz_history.save()


    def delete(self, *args):
        quiz_history = self.get_history_ent()
        quiz_history.is_deleted = True
        quiz_history.save()
        super(QuizRating, self).delete(*args)

    
    objects = QuizRatingManager()


class QuizHistory(models.Model):
    date = models.DateTimeField()
    theory = models.IntegerField()
    practice = models.IntegerField()
    topic_id = models.IntegerField()
    student_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
class RealTestManager(models.Manager):
    pass

class RealTest(models.Model):
    date = models.DateField()
    score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    # owner

    def get_history_ent(self):
        return RealTestHistory(
            date = self.date,
            score = self.score,
            subject_id = self.subject.pk,
            student_id = self.student.pk,
            created_date = self.created_date,
            origin_id = self.pk,
        )


    def save(self, *args, **kwargs):
        super(RealTest, self).save(*args, **kwargs)
        test_history = self.get_history_ent()
        test_history.is_deleted = False
        test_history.save()


    def delete(self, *args):
        test_history = self.get_history_ent()
        test_history.is_deleted = True
        test_history.save()
        super(RealTest, self).delete(*args)




class RealTestHistory(models.Model):
    date = models.DateField()
    score = models.IntegerField()
    subject_id = models.IntegerField()
    student_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    #owner

    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


    objects = RealTestManager()
# class TestResult(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)