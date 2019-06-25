from django.contrib import admin
from .models import Subtopic, Subject, Topic, SubjectHistory, TopicHistory

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_quiz', 'subject')

class SubjectHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'origin_id', 'updated_date', 'is_deleted')

class TopicHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_quiz', 'subject_id', 'created_date', 'origin_id', 'updated_date', 'is_deleted')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Subtopic)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SubjectHistory, SubjectHistoryAdmin)
admin.site.register(TopicHistory, TopicHistoryAdmin)
