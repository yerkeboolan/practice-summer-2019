from django.urls import path
from . import views

urlpatterns = [
    path('subject_list/', views.subject_list),
    path('topic_list/', views.topic_list),
    path('subtopic_list/', views.subtopic_list),
    path('subject_topic_list/', views.subject_topic_view),
    path('topic_subtopic_list/', views.topic_subtopic_view),
    path('subject_view/', views.general_view),
    path('subject/', views.SubjectList.as_view()),
    path('subject/<pk>/', views.SubjectList.as_view()),
    path('topic/', views.TopicList.as_view()),
    path('topic/<pk>/', views.TopicList.as_view()),
    path('subtopics/', views.SubtopicList.as_view()),
    path('subtopic/', views.SubtopicDetail.as_view()),
    path('subtopic/<pk>/', views.SubtopicDetail.as_view())
]