from rest_framework import serializers
from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    """List of tasks"""

    class Meta:
        model = Task
        fields = ['title', 'task']