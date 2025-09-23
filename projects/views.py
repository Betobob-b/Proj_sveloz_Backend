from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import filters
from rest_framework import permissions

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)