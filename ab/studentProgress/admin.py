from django.contrib import admin
from .models import GroupAttendance, StudentAttendance, QuizRating, RealTest, QuizHistory, RealTestHistory, GroupAttendanceHistory, StudentAttendanceHistory

# Register your models here.


class GroupAttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'group', )

class GroupAttendanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'group_id', 'created_date', 'origin_id', 'updated_date', 'is_deleted', )


class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'att', 'rating', 'group_att',  'group_student', )


class StudentAttendanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'att', 'rating', 'group_att_id', 'group_student_id', 'created_date', 'updated_date', 'origin_id', 'is_deleted')


class QuizRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'theory', 'practice', 'topic', 'student', )

class QuizHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'origin_id', 'created_date', 'theory', 'practice', 'topic_id', 'student_id', 'updated_date', 'is_deleted')

class RealTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'score', 'subject', 'student', )

class RealTestHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'origin_id', 'created_date', 'score', 'subject_id', 'student_id', 'updated_date', 'is_deleted')

admin.site.register(GroupAttendance, GroupAttendanceAdmin)
admin.site.register(StudentAttendance, StudentAttendanceAdmin)
admin.site.register(GroupAttendanceHistory, GroupAttendanceHistoryAdmin)
admin.site.register(StudentAttendanceHistory, StudentAttendanceHistoryAdmin)
admin.site.register(QuizRating, QuizRatingAdmin)
admin.site.register(QuizHistory, QuizHistoryAdmin)
admin.site.register(RealTest, RealTestAdmin)
admin.site.register(RealTestHistory, RealTestHistoryAdmin)