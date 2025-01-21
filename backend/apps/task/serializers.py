import logging
from datetime import datetime

from core.services.task_manager_service import TaskService

from django.db.transaction import atomic

from rest_framework import serializers

from apps.task.choices import TaskStatusChoice
from apps.task.models import TaskModel
from apps.users.serializers import UserSerializer

logger = logging.getLogger()


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskModel
        fields = (
            'id', 'description', 'priority', 'status', 'created_by_user', 'finished_at', 'user', 'created_at',
            'updated_at')
        read_only_fields = ('id', 'finished_at', 'created_by_user', 'created_at', 'updated_at')

    @atomic
    def create(self, validated_data):
        task = super().create(validated_data)
        TaskService.handle_task(task.id)
        return task


class TaskUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskModel
        fields = (
            'id', 'description', 'priority', 'status', 'created_by_user', 'finished_at', 'user', 'created_at',
            'updated_at')
        read_only_fields = ('id', 'finished_at', 'created_by_user', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        new_status = validated_data.get('status')

        if new_status == TaskStatusChoice.Completed and instance.status != TaskStatusChoice.Completed:
            instance.finished_at = datetime.now()
        return super().update(instance, validated_data)
