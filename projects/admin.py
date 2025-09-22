from django.contrib import admin
from .models import Project

#admin.site.register(Project)

class ProjectAdmin(admin.ModelAdmin):

    readonly_fields = ('creator',)

    def save_model(self, request, obj, form, change):

        if not obj.pk:

            obj.creator = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Project, ProjectAdmin)
