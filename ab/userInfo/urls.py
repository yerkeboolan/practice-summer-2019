from django.urls import path
from userInfo import views

urlpatterns = [
    path('students/full_info/', views.StudentListFullInfo.as_view()),
    path('student/<pk>/full_info/', views.StudentDetailFullInfo.as_view()),
    path('student_status/<pk>/', views.StudentDetail.as_view()),

    path('student/', views.StudentDetail.as_view()),

    path('student/<student_pk>/groups/', views.StudentGroupFullInfo.as_view()),


    path('teachers/', views.TeacherList.as_view()),
    path('teacher/', views.TeacherDetail.as_view())
]