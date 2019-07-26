from django.contrib import admin
from .models import VideoAccess, TestAccess

# Register your models here.

admin.site.register(VideoAccess)
admin.site.register(TestAccess)