from django.urls import path
from access.views import VideoAccessDetail, TestAccessDetail

urlpatterns = [
    path('video_access/', VideoAccessDetail.as_view()),
    path('video_access/<pk>/', VideoAccessDetail.as_view()),

    path('test_access/', TestAccessDetail.as_view())
]