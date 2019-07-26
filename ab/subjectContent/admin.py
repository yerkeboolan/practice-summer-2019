from django.contrib import admin
from .models import Test, Question, Answer, Video

# Register your models here.

admin.site.register(Video)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)