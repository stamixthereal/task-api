from rest_framework import serializers
from .models import Task, Message


class FilterReviewListSerializer(serializers.ListSerializer):
    """Filter messages, only parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Recursively output children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


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

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Message
        fields = ["user", "text", "children"]


class TaskDetailSerializer(serializers.ModelSerializer):
    """Detail view of certain task"""

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    messages = MessageSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'