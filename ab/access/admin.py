from django.contrib import admin
from .models import Video, VideoAccess, TestAccess

# Register your models here.


admin.site.register(Video)
admin.site.register(VideoAccess)
admin.site.register(TestAccess)