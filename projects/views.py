from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import filters

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']