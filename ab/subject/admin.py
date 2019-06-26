from django.contrib import admin
from .models import Subtopic, Subject, Topic, SubjectHistory, TopicHistory, SubtopicHistory

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_quiz', 'subject')

class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic')

class SubjectHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'origin_id', 'updated_date', 'is_deleted')

class TopicHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_quiz', 'subject_id', 'created_date', 'origin_id', 'updated_date', 'is_deleted')

class SubtopicHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic_id', 'created_date', 'origin_id', 'updated_date', 'is_deleted')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Subtopic, SubtopicAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(SubjectHistory, SubjectHistoryAdmin)
admin.site.register(TopicHistory, TopicHistoryAdmin)
admin.site.register(SubtopicHistory, SubtopicHistoryAdmin)
