from re import M
from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.TaskListView.as_view()),
    path('tasks/task_<int:pk>/', views.TaskDetailView.as_view()),
    path('message/', views.MessageCreateView.as_view())
]