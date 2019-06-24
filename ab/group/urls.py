from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('group/', views.GroupDetail.as_view()),
    path('group/<pk>/', views.GroupDetail.as_view()),
    path('groupStudents/', views.GroupStudentList.as_view()),
    path('groupStudent/', views.GroupStudentDetail.as_view()),
    path('groupStudent/<pk>/', views.GroupStudentDetail.as_view())
]