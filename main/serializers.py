from rest_framework import serializers
from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    """List of tasks"""

    class Meta:
        model = Task
        fields = ['title', 'task']


class TaskDetailSerializer(serializers.ModelSerializer):
    """Detail view of certain task"""

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Task
        exclude = ['id', 'publish']