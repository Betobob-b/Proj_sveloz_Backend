from django.contrib import admin
from .models import Task

#admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):

    readonly_fields = ('responsible',)

    def save_model(self, request, obj, form, change):

        if not obj.pk:
            obj.responsible = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)