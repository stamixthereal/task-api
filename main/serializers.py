from rest_framework import serializers
from .models import Task, Message


class TaskListSerializer(serializers.ModelSerializer):
    """List of tasks"""

    class Meta:
        model = Task
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    """Creating message"""

    class Meta:
        model = Message
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """Viewing messages"""

    class Meta:
        model = Message
        fields = ['user', 'text']


class TaskDetailSerializer(serializers.ModelSerializer):
    """Detail view of certain task"""

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    messages = MessageSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'