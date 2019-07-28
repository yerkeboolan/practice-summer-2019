from django.contrib import admin
from .models import Test, Question, Answer, Video, VideoHistory

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'subtopic', )


class VideoHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'subtopic_id', 'origin_id', 'created_date', 'updated_date', 'is_deleted', )



admin.site.register(Video, VideoAdmin)
admin.site.register(VideoHistory, VideoHistoryAdmin)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)