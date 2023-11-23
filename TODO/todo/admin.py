from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('Task', 'is_completed', 'updated_at')
    search_fields = ('Task',)

admin.site.register(Task, TaskAdmin)