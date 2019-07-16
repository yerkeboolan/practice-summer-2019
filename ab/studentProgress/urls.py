from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<pk>/', views.QuizDetail.as_view()),
    path('quiz/', views.QuizDetail.as_view()),

    path('test/<pk>/', views.RealTestDetail.as_view()),
    path('test/', views.RealTestDetail.as_view())
]