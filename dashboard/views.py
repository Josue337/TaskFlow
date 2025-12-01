from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from projects.models import Project
from tasks.models import Task, ActivityLog
import json

# US15: Dashboard principal
@login_required
def dashboard_home(request):
    """Vista principal del dashboard - US15, US18, US19, US20"""
    
    # Proyectos del usuario
    user_projects = Project.objects.filter(
        Q(members=request.user) | Q(creator=request.user)
    ).distinct().exclude(status='archived')
    
    # Tareas asignadas al usuario
    user_tasks = Task.objects.filter(assigned_to=request.user)
    
    # Tareas recientes (últimas 10)
    recent_tasks = user_tasks.order_by('-updated_at')[:10]
    
    # Tareas por estado
    tasks_todo = user_tasks.filter(status='todo').count()
    tasks_in_progress = user_tasks.filter(status='in_progress').count()
    tasks_done = user_tasks.filter(status='done').count()
    
    # Tareas por prioridad
    tasks_by_priority = {
        'urgent': user_tasks.filter(priority='urgent').count(),
        'high': user_tasks.filter(priority='high').count(),
        'medium': user_tasks.filter(priority='medium').count(),
        'low': user_tasks.filter(priority='low').count(),
    }
    
    # Actividad reciente global (US20)
    recent_activity = ActivityLog.objects.filter(
        project__in=user_projects
    ).order_by('-created_at')[:15]
    
    # Estadísticas de proyectos
    active_projects = user_projects.filter(status='active').count()
    completed_projects = user_projects.filter(status='completed').count()
    
    # Datos para gráficos (US19)
    chart_data = {
        'tasks_by_status': {
            'labels': ['Por Hacer', 'En Progreso', 'Completado'],
            'data': [tasks_todo, tasks_in_progress, tasks_done]
        },
        'tasks_by_priority': {
            'labels': ['Urgente', 'Alta', 'Media', 'Baja'],
            'data': [
                tasks_by_priority['urgent'],
                tasks_by_priority['high'],
                tasks_by_priority['medium'],
                tasks_by_priority['low']
            ]
        }
    }
    
    context = {
        'projects': user_projects[:5],  # Últimos 5 proyectos
        'recent_tasks': recent_tasks,
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_done': tasks_done,
        'tasks_by_priority': tasks_by_priority,
        'recent_activity': recent_activity,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'total_tasks': user_tasks.count(),
        'chart_data': json.dumps(chart_data),
    }
    
    return render(request, 'dashboard/home.html', context)


# Vista de estadísticas (US18, US19)
@login_required
def statistics_view(request):
    """Vista detallada de estadísticas"""
    
    # Proyectos del usuario
    user_projects = Project.objects.filter(
        Q(members=request.user) | Q(creator=request.user)
    ).distinct()
    
    # Estadísticas por proyecto
    project_stats = []
    for project in user_projects.exclude(status='archived'):
        stats = {
            'project': project,
            'progress': project.get_progress_percentage(),
            'tasks_by_status': project.get_tasks_by_status(),
            'total_tasks': project.tasks.count(),
            'members_count': project.members.count(),
        }
        project_stats.append(stats)
    
    # Tareas del usuario
    user_tasks = Task.objects.filter(assigned_to=request.user)
    
    # Gráficos
    chart_data = {
        'projects_by_status': {
            'labels': ['Activos', 'Completados', 'En Pausa', 'Archivados'],
            'data': [
                user_projects.filter(status='active').count(),
                user_projects.filter(status='completed').count(),
                user_projects.filter(status='on_hold').count(),
                user_projects.filter(status='archived').count(),
            ]
        },
        'my_tasks_status': {
            'labels': ['Por Hacer', 'En Progreso', 'Completado'],
            'data': [
                user_tasks.filter(status='todo').count(),
                user_tasks.filter(status='in_progress').count(),
                user_tasks.filter(status='done').count(),
            ]
        }
    }
    
    context = {
        'project_stats': project_stats,
        'total_projects': user_projects.count(),
        'total_tasks': user_tasks.count(),
        'chart_data': json.dumps(chart_data),
    }
    
    return render(request, 'dashboard/statistics.html', context)
