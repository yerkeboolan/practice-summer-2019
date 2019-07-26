from django.urls import path
from subjectContent.views import VideoList, VideoDetail, TestList, TestDetail, QuestionList, QuestionDetail

urlpatterns = [
    path('videos/', VideoList.as_view()),
    path('video/', VideoDetail.as_view()),
    path('video/<pk>/', VideoDetail.as_view()),


    path('tests/', TestList.as_view()),
    path('test/', TestDetail.as_view()),
    path('test/<pk>/', TestDetail.as_view()),

    path('questions/<test_pk>/', QuestionList.as_view()),
    path('question/', QuestionDetail.as_view())
]