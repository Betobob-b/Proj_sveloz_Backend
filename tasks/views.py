from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'status']

    def get_queryset(self):

        user_queryset = Task.objects.filter(project__creator=self.request.user)
        project_id = self.request.query_params.get('project')

        if project_id is not None:
            return user_queryset.filter(project_id=project_id)

        return user_queryset

    def perform_create(self, serializer):
        serializer.save(responsible=self.request.user)