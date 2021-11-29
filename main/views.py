from .models import Message, Task
from .serializers import TaskListSerializer, MessageCreateSerializer
from rest_framework import viewsets, mixins

class TaskView(
            mixins.ListModelMixin, 
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = TaskListSerializer
    queryset = Task.objects.all()


class MessageView(
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()