from django.contrib import admin
from .models import GroupAttendance, StudentAttendance, QuizRating, RealTest, QuizHistory, RealTestHistory

# Register your models here.


class QuizRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'theory', 'practice', 'topic', 'student', )

class QuizHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'origin_id', 'created_date', 'theory', 'practice', 'topic_id', 'student_id', 'updated_date', 'is_deleted')

class RealTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'score', 'subject', 'student', )

class RealTestHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'origin_id', 'created_date', 'score', 'subject_id', 'student_id', 'updated_date', 'is_deleted')

admin.site.register(GroupAttendance)
admin.site.register(StudentAttendance)
admin.site.register(QuizRating, QuizRatingAdmin)
admin.site.register(QuizHistory, QuizHistoryAdmin)
admin.site.register(RealTest, RealTestAdmin)
admin.site.register(RealTestHistory, RealTestHistoryAdmin)