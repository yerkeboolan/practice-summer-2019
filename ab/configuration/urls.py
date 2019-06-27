from django.urls import path
from configuration import views

urlpatterns = [
    path('userStatuses/', views.UserStatusConfigList.as_view()),
    path('userStatus/', views.UserStatusConfigDetail.as_view()),
    path('userStatus/<pk>/', views.UserStatusConfigDetail.as_view())
]