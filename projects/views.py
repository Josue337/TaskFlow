from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Project, ProjectInvitation
from .forms import ProjectForm, ProjectInvitationForm
from tasks.models import ActivityLog

# US5: Crear proyecto
@login_required
def project_create(request):
    """Vista para crear un proyecto"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            project.members.add(request.user)
            messages.success(request, f'Proyecto "{project.name}" creado exitosamente.')
            return redirect('projects:detail', pk=project.pk)
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})


# Lista de proyectos
@login_required
def project_list(request):
    """Vista para listar proyectos"""
    # Proyectos donde el usuario es miembro o creador
    projects = Project.objects.filter(
        Q(members=request.user) | Q(creator=request.user)
    ).distinct().exclude(status='archived')
    
    # Filtros
    status_filter = request.GET.get('status')
    if status_filter:
        projects = projects.filter(status=status_filter)
    
    context = {
        'projects': projects,
        'active_projects': projects.filter(status='active').count(),
        'completed_projects': projects.filter(status='completed').count(),
    }
    return render(request, 'projects/project_list.html', context)


# Detalle del proyecto
@login_required
def project_detail(request, pk):
    """Vista para ver el detalle de un proyecto - US18, US19"""
    project = get_object_or_404(Project, pk=pk)
    
    # Verificar que el usuario tiene acceso
    if request.user not in project.members.all() and project.creator != request.user:
        messages.error(request, 'No tienes acceso a este proyecto.')
        return redirect('projects:list')
    
    # Obtener tareas del proyecto
    tasks = project.tasks.all()
    
    # Estadísticas
    tasks_by_status = project.get_tasks_by_status()
    progress = project.get_progress_percentage()
    
    # Actividad reciente - US20
    recent_activity = project.activity_logs.all()[:10]
    
    context = {
        'project': project,
        'tasks': tasks,
        'tasks_by_status': tasks_by_status,
        'progress': progress,
        'recent_activity': recent_activity,
    }
    return render(request, 'projects/project_detail.html', context)


# US6: Editar proyecto
@login_required
def project_update(request, pk):
    """Vista para editar un proyecto"""
    project = get_object_or_404(Project, pk=pk)
    
    # Solo el creador o admins pueden editar
    if project.creator != request.user and not request.user.is_admin():
        messages.error(request, 'No tienes permiso para editar este proyecto.')
        return redirect('projects:detail', pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto actualizado exitosamente.')
            return redirect('projects:detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    
    context = {
        'form': form,
        'project': project,
        'is_edit': True
    }
    return render(request, 'projects/project_form.html', context)


# US8: Archivar proyecto
@login_required
def project_archive(request, pk):
    """Vista para archivar/desarchivar un proyecto"""
    project = get_object_or_404(Project, pk=pk)
    
    if project.creator != request.user and not request.user.is_admin():
        messages.error(request, 'No tienes permiso para archivar este proyecto.')
        return redirect('projects:detail', pk=pk)
    
    if project.status == 'archived':
        project.status = 'active'
        messages.success(request, f'Proyecto "{project.name}" desarchivado.')
    else:
        project.status = 'archived'
        messages.success(request, f'Proyecto "{project.name}" archivado.')
    
    project.save()
    return redirect('projects:list')


# US7: Agregar miembros al proyecto
@login_required
def project_invite(request, pk):
    """Vista para invitar miembros a un proyecto"""
    project = get_object_or_404(Project, pk=pk)
    
    if project.creator != request.user and not request.user.is_admin():
        messages.error(request, 'No tienes permiso para invitar miembros.')
        return redirect('projects:detail', pk=pk)
    
    if request.method == 'POST':
        form = ProjectInvitationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Verificar si el usuario existe
            from users.models import CustomUser
            try:
                user = CustomUser.objects.get(email=email)
                
                # Verificar si ya es miembro
                if user in project.members.all():
                    messages.warning(request, f'{email} ya es miembro del proyecto.')
                else:
                    project.members.add(user)
                    messages.success(request, f'{email} agregado al proyecto exitosamente.')
                    
                    # Registrar actividad
                    ActivityLog.objects.create(
                        project=project,
                        user=request.user,
                        action='task_assigned',
                        description=f'{request.user.username} agregó a {user.username} al proyecto'
                    )
            except CustomUser.DoesNotExist:
                # Crear invitación
                invitation, created = ProjectInvitation.objects.get_or_create(
                    project=project,
                    email=email,
                    defaults={'invited_by': request.user}
                )
                if created:
                    messages.success(
                        request, 
                        f'Invitación enviada a {email}. Deberán registrarse para unirse.'
                    )
                else:
                    messages.info(request, f'Ya existe una invitación pendiente para {email}.')
            
            return redirect('projects:detail', pk=pk)
    else:
        form = ProjectInvitationForm()
    
    context = {
        'form': form,
        'project': project,
        'invitations': project.invitations.filter(status='pending')
    }
    return render(request, 'projects/project_invite.html', context)


# Proyectos archivados
@login_required
def project_archived_list(request):
    """Vista para listar proyectos archivados"""
    projects = Project.objects.filter(
        Q(members=request.user) | Q(creator=request.user),
        status='archived'
    ).distinct()
    
    context = {'projects': projects}
    return render(request, 'projects/project_archived.html', context)
