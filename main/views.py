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

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MessageView(
            mixins.ListModelMixin, 
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet
            ):

    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()

    def post(self, request, *args, **kwargs):
        message = MessageCreateSerializer(data=request.data)
        if message.is_valid():
            message.save()
        return self.create(request, *args, **kwargs)