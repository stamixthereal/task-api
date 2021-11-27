from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    """Model of each task"""

    STATUS_CHOICES = (
                    ('Frozen', 'Frozen'),
                    ('Done', 'Done'),
                    ('Undone', 'Undone')
                    )
                    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Name', max_length=255)
    task = models.TextField('Description')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
                            max_length=10,
                            choices=STATUS_CHOICES,
                            default='Undone')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'TASK'
        verbose_name_plural = 'TASKS'


class Message(models.Model):
    """Model of each message"""

    user = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey("self", verbose_name="parent", on_delete=models.SET_NULL, blank=True, null=True)
    task = models.ForeignKey(Task, verbose_name="task", on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return f"{self.user} - {self.task}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"