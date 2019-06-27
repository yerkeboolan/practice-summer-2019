from django.contrib import admin
from .models import UserStatusConfig, UserStatusConfigHistory

# Register your models here.

class UserStatusConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'is_active')

class UserStatusConfigHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'is_active', 'origin_id', 'created_date', 'updated_date', 'is_deleted')



admin.site.register(UserStatusConfig, UserStatusConfigAdmin)
admin.site.register(UserStatusConfigHistory, UserStatusConfigHistoryAdmin)
