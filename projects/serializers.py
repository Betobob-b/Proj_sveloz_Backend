from rest_framework import serializers
from .models import Project
from tasks.serializers import TaskSerializer

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'creator', 'created_at', 'tasks']

        read_only_fields = ['creator', 'created_at', 'tasks']