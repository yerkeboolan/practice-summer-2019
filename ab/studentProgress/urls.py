from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<pk>/', views.QuizDetail.as_view()),
    path('quiz/', views.QuizDetail.as_view()),

    path('test/<pk>/', views.RealTestDetail.as_view()),
    path('test/', views.RealTestDetail.as_view()),

    path('get/attendance/<group_pk>/', views.GroupAttendanceList.as_view()),
    path('set/attendance/', views.GroupAttendanceDetail.as_view()),
    path('update/attendance/<group_pk>/', views.GroupAttendanceDetail.as_view())
]