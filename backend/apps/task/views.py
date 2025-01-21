import logging
from datetime import datetime

from core.permissions.user_permissions import IsOwnerPermission, IsOwnerPermissionOrReadOnly

from django.db.models import Count

from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.task.choices import TaskStatusChoice
from apps.task.filters import TaskFilter
from apps.task.models import TaskModel
from apps.task.serializers import TaskSerializer, TaskUpdateSerializer

logger = logging.getLogger()


class TaskListCreateView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = TaskFilter

    def perform_create(self, serializer):
        serializer.save(created_by_user=self.request.user)


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.select_related('user').all()
    serializer_class = TaskUpdateSerializer
    permission_classes = (IsOwnerPermissionOrReadOnly,)



class ListUsersTasksView(ListAPIView):
    permission_classes = (IsOwnerPermission,)
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.select_related('user').all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class TaskStatisticView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

    def get(self, request, *args, **kwargs):
        total_tasks = self.get_queryset().count()
        status_counts = self.get_queryset().values('status').annotate(count=Count('status'))
        statistics = {
            'total_tasks': total_tasks,
            'statuses': {entry['status']: entry['count'] for entry in status_counts},
        }

        return Response(statistics, status=status.HTTP_200_OK)
