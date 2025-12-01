from django.contrib import admin
from .models import Project, ProjectInvitation

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'status', 'created_at', 'get_members_count']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'description', 'creator__username']
    filter_horizontal = ['members']
    date_hierarchy = 'created_at'
    
    def get_members_count(self, obj):
        return obj.members.count()
    get_members_count.short_description = 'Miembros'


@admin.register(ProjectInvitation)
class ProjectInvitationAdmin(admin.ModelAdmin):
    list_display = ['project', 'email', 'invited_by', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['email', 'project__name']
    date_hierarchy = 'created_at'
