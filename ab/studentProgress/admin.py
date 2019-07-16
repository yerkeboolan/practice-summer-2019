from django.contrib import admin
from .models import GroupAttendance, StudentAttendance, QuizRating, RealTest, QuizHistory

# Register your models here.


class QuizRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'theory', 'practice', 'topic', 'student', )

class QuizHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'origin_id', 'created_date', 'theory', 'practice', 'topic_id', 'student_id', 'updated_date', 'is_deleted')


admin.site.register(GroupAttendance)
admin.site.register(StudentAttendance)
admin.site.register(QuizRating, QuizRatingAdmin)
admin.site.register(QuizHistory, QuizHistoryAdmin)
admin.site.register(RealTest)
