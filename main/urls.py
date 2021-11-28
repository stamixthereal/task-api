from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tasks', views.TaskView, basename='tasks')
router.register('message', views.MessageView, basename='message')

urlpatterns = router.urls