from django.contrib import admin
from .models import Task, TaskComment, TaskAttachment, ActivityLog

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'created_by', 'status', 'priority', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'created_at', 'due_date']
    search_fields = ['title', 'description', 'project__name']
    filter_horizontal = ['assigned_to']
    date_hierarchy = 'created_at'


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'task__title', 'author__username']
    date_hierarchy = 'created_at'


@admin.register(TaskAttachment)
class TaskAttachmentAdmin(admin.ModelAdmin):
    list_display = ['task', 'file', 'uploaded_by', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['task__title', 'description']
    date_hierarchy = 'uploaded_at'


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'action', 'task', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['description', 'project__name', 'user__username']
    date_hierarchy = 'created_at'
