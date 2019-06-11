from django.contrib import admin
from .models import UserInfo, Teacher, Student, Subject, Topic, Subtopic, Group, GroupStudent, Date, Attendance, Video, VideoAccess, Test, TestAccess, Question, Answer, QuizRating, RealTest, TestResult

# Register your models here.


admin.site.register(UserInfo)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Group)
admin.site.register(GroupStudent)
admin.site.register(Date)
admin.site.register(Attendance)
admin.site.register(Video)
admin.site.register(VideoAccess)
admin.site.register(Test)
admin.site.register(TestAccess)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizRating)
admin.site.register(RealTest)
admin.site.register(TestResult)
