from core.permissions.user_permissions import IsOwnerPermissionOrReadOnly

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import MentoringServiceModel
from .serializers import MentoringServiceSerializer


class MentoringServiceViewSet(ModelViewSet):
    queryset = MentoringServiceModel.objects.all()
    serializer_class = MentoringServiceSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermissionOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

