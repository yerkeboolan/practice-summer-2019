from django.db import models
from userInfo.models import Teacher, Student
from subject.models import Subject


# Create your models here.

class GroupManager(models.Manager):
    pass

class Group(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    # owner

    def get_history_ent(self):
        return GroupHistory(
            title = self.title,
            subject_id = self.subject.pk,
            teacher_id = self.teacher.pk,
            created_date = self.created_date,
            origin_id = self.pk
        )

    def save(self, *args, **kwargs):
        super(Group, self).save(*args, **kwargs)
        group_history = self.get_history_ent()
        group_history.is_deleted = False
        group_history.save()


    def delete(self, *args):
        group_history = self.get_history_ent()
        group_history.is_deleted = True
        group_history.save()
        super(Group, self).delete(*args)


    def __str__(self):
        return self.title

    objects = GroupManager()


class GroupHistory(models.Model):
    title = models.CharField(max_length=255)
    subject_id = models.IntegerField()
    teacher_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # owner
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now = False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class GroupStudentManager(models.Manager):
        pass


class GroupStudentHistory(models.Model):
    student_id = models.IntegerField()
    group_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    #owner
    origin_id = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class GroupStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    # owner

    def get_history_ent(self):
        return GroupStudentHistory (
            student_id = self.student.pk,
            group_id = self.group.pk,
            created_date = self.created_date,
            origin_id = self.pk
        )


    def save(self, *args, **kwargs):
        super(GroupStudent, self).save(*args, **kwargs)
        groupStudent_history = self.get_history_ent()
        groupStudent_history.is_deleted = False
        groupStudent_history.save()


    def delete(self, *args):
        groupStudent_history = self.get_history_ent()
        groupStudent_history.is_deleted = True
        groupStudent_history.save()
        super(GroupStudent, self).delete(*args)


    objects = GroupStudentManager()