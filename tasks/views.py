from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Task, TaskComment, TaskAttachment, ActivityLog
from .forms import TaskForm, TaskCommentForm, TaskAttachmentForm
from projects.models import Project

# US9: Crear tarea
@login_required
def task_create(request, project_pk):
    """Vista para crear una tarea"""
    project = get_object_or_404(Project, pk=project_pk)
    
    # Verificar acceso
    if request.user not in project.members.all() and project.creator != request.user:
        messages.error(request, 'No tienes acceso a este proyecto.')
        return redirect('projects:list')
    
    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = request.user
            task.save()
            form.save_m2m()  # Guardar relaciones many-to-many
            
            # Registrar actividad
            ActivityLog.objects.create(
                project=project,
                user=request.user,
                action='task_created',
                description=f'{request.user.username} creó la tarea "{task.title}"',
                task=task
            )
            
            messages.success(request, f'Tarea "{task.title}" creada exitosamente.')
            return redirect('projects:detail', pk=project.pk)
    else:
        form = TaskForm(project=project)
    
    context = {
        'form': form,
        'project': project
    }
    return render(request, 'tasks/task_form.html', context)


# Detalle de tarea
@login_required
def task_detail(request, pk):
    """Vista para ver el detalle de una tarea - US12, US13"""
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    
    # Verificar acceso
    if request.user not in project.members.all() and project.creator != request.user:
        messages.error(request, 'No tienes acceso a esta tarea.')
        return redirect('projects:list')
    
    # Formularios
    comment_form = TaskCommentForm()
    attachment_form = TaskAttachmentForm()
    
    # Manejar comentarios
    if request.method == 'POST' and 'add_comment' in request.POST:
        comment_form = TaskCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                project=project,
                user=request.user,
                action='comment_added',
                description=f'{request.user.username} comentó en "{task.title}"',
                task=task
            )
            
            messages.success(request, 'Comentario agregado.')
            return redirect('tasks:detail', pk=pk)
    
    # Manejar archivos adjuntos
    if request.method == 'POST' and 'add_attachment' in request.POST:
        attachment_form = TaskAttachmentForm(request.POST, request.FILES)
        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.task = task
            attachment.uploaded_by = request.user
            attachment.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                project=project,
                user=request.user,
                action='file_uploaded',
                description=f'{request.user.username} subió un archivo a "{task.title}"',
                task=task
            )
            
            messages.success(request, 'Archivo adjuntado exitosamente.')
            return redirect('tasks:detail', pk=pk)
    
    context = {
        'task': task,
        'project': project,
        'comments': task.comments.all(),
        'attachments': task.attachments.all(),
        'comment_form': comment_form,
        'attachment_form': attachment_form,
    }
    return render(request, 'tasks/task_detail.html', context)


# US9, US10: Editar tarea
@login_required
def task_update(request, pk):
    """Vista para editar una tarea"""
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    
    # Verificar acceso
    if request.user not in project.members.all() and project.creator != request.user:
        messages.error(request, 'No tienes permiso para editar esta tarea.')
        return redirect('projects:list')
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project=project)
        if form.is_valid():
            form.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                project=project,
                user=request.user,
                action='task_updated',
                description=f'{request.user.username} actualizó la tarea "{task.title}"',
                task=task
            )
            
            messages.success(request, 'Tarea actualizada exitosamente.')
            return redirect('tasks:detail', pk=pk)
    else:
        form = TaskForm(instance=task, project=project)
    
    context = {
        'form': form,
        'task': task,
        'project': project,
        'is_edit': True
    }
    return render(request, 'tasks/task_form.html', context)


# US11: Cambiar estado de tarea
@login_required
def task_change_status(request, pk):
    """Vista para cambiar el estado de una tarea"""
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    
    # Verificar acceso
    if request.user not in project.members.all() and project.creator != request.user:
        messages.error(request, 'No tienes permiso para cambiar el estado.')
        return redirect('projects:list')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        old_status = task.status
        
        if new_status in ['todo', 'in_progress', 'done']:
            task.status = new_status
            
            # Si se completa, registrar fecha
            if new_status == 'done' and old_status != 'done':
                task.completed_at = timezone.now()
                
                # Registrar actividad
                ActivityLog.objects.create(
                    project=project,
                    user=request.user,
                    action='task_completed',
                    description=f'{request.user.username} completó la tarea "{task.title}"',
                    task=task
                )
            else:
                # Registrar cambio de estado
                ActivityLog.objects.create(
                    project=project,
                    user=request.user,
                    action='status_changed',
                    description=f'{request.user.username} cambió "{task.title}" de {task.get_status_display()} a {dict(Task.STATUS_CHOICES)[new_status]}',
                    task=task
                )
            
            task.save()
            messages.success(request, f'Estado cambiado a {task.get_status_display()}.')
    
    return redirect('tasks:detail', pk=pk)


# Eliminar tarea
@login_required
def task_delete(request, pk):
    """Vista para eliminar una tarea"""
    task = get_object_or_404(Task, pk=pk)
    project = task.project
    
    # Solo el creador o admin puede eliminar
    if task.created_by != request.user and not request.user.is_admin():
        messages.error(request, 'No tienes permiso para eliminar esta tarea.')
        return redirect('tasks:detail', pk=pk)
    
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Tarea "{task_title}" eliminada exitosamente.')
        return redirect('projects:detail', pk=project.pk)
    
    context = {
        'task': task,
        'project': project
    }
    return render(request, 'tasks/task_confirm_delete.html', context)


# Eliminar comentario
@login_required
def comment_delete(request, pk):
    """Vista para eliminar un comentario"""
    comment = get_object_or_404(TaskComment, pk=pk)
    task_pk = comment.task.pk
    
    # Solo el autor o admin puede eliminar
    if comment.author != request.user and not request.user.is_admin():
        messages.error(request, 'No tienes permiso para eliminar este comentario.')
        return redirect('tasks:detail', pk=task_pk)
    
    comment.delete()
    messages.success(request, 'Comentario eliminado.')
    return redirect('tasks:detail', pk=task_pk)


# Eliminar archivo adjunto
@login_required
def attachment_delete(request, pk):
    """Vista para eliminar un archivo adjunto"""
    attachment = get_object_or_404(TaskAttachment, pk=pk)
    task_pk = attachment.task.pk
    
    # Solo el uploader o admin puede eliminar
    if attachment.uploaded_by != request.user and not request.user.is_admin():
        messages.error(request, 'No tienes permiso para eliminar este archivo.')
        return redirect('tasks:detail', pk=task_pk)
    
    attachment.file.delete()  # Eliminar archivo físico
    attachment.delete()
    messages.success(request, 'Archivo eliminado.')
    return redirect('tasks:detail', pk=task_pk)
