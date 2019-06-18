from django.contrib import admin
from .models import Subtopic, Subject, Topic

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_quiz', 'subject')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Subtopic)
admin.site.register(Topic, TopicAdmin)
