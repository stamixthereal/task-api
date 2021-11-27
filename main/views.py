from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer, MessageCreateSerializer


class TaskListView(APIView):
    """Task list output"""

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):
    """Task detail output"""

    def get(self, request, pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(tasks, many=False)
        return Response(serializer.data)


class MessageCreateView(APIView):
    """Creating message to task"""

    def post(self, request):
        message = MessageCreateSerializer(data=request.data)
        if message.is_valid():
            message.save()
        return Response(status=201)