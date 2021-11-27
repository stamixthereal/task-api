from re import T
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskListSerializer


class TaskListView(APIView):
    """Task list output"""

    def get(self, request):
        tasks = Task.objects.filter(id=True)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)