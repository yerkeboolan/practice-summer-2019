from django.contrib import admin
from .models import GroupStudent, Group, GroupHistory, GroupStudentHistory

# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'teacher')

class GroupStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group')

class GroupHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject_id', 'teacher_id', 'origin_id', 'created_date', 'updated_date', 'is_deleted')

class GroupStudentHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'group_id', 'origin_id', 'created_date', 'updated_date', 'is_deleted')

admin.site.register(GroupStudent, GroupStudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupHistory, GroupHistoryAdmin)
admin.site.register(GroupStudentHistory, GroupStudentHistoryAdmin)

