from django.contrib import admin
from .models import Date, Attendance, QuizRating, RealTest

# Register your models here.


admin.site.register(Date)
admin.site.register(Attendance)
admin.site.register(QuizRating)
admin.site.register(RealTest)
