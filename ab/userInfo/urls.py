from django.urls import path
from userInfo import views

urlpatterns = [
    path('students/full_info/', views.StudentListFullInfo.as_view()),
    path('student/<pk>/full_info/', views.StudentDetailFullInfo.as_view()),
    path('student_status/<pk>/', views.StudentDetail.as_view())
]