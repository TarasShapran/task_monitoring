from core.models import BaseModel

from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from apps.task.choices import TaskStatusChoice
from apps.task.managers import TaskManager

UserModel = get_user_model()

class TaskModel(BaseModel):
    class Meta:
        db_table = 'tasks'
        ordering = ['-created_at']

    description = models.CharField(max_length=500)
    priority = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(5)])
    status = models.CharField(max_length=20, choices=TaskStatusChoice.choices, default=TaskStatusChoice.Pending)
    finished_at = models.DateTimeField(null=True)
    created_by_user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='created_tasks')
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='tasks', null=True)

    objects = TaskManager
