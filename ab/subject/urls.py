from django.urls import path
from . import views

urlpatterns = [
    path('subject_list/', views.subject_list),
    path('topic_list/', views.topic_list),
    path('subtopic_list/', views.subtopic_list)
]