from rest_framework import serializers

from .models import MentoringServiceModel


class MentoringServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentoringServiceModel
        fields = ['id', 'title', 'description', 'price', 'user']
        read_only_fields = ['user']