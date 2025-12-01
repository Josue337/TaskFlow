from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):
    """
    Modelo para tareas - US9, US10, US11, US13
    """
    STATUS_CHOICES = [
        ('todo', 'Por Hacer'),
        ('in_progress', 'En Progreso'),
        ('done', 'Completado'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('urgent', 'Urgente'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Proyecto'
    )
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='assigned_tasks',
        blank=True,
        verbose_name='Asignado a'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks',
        verbose_name='Creado por'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo',
        verbose_name='Estado'
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='Prioridad'
    )
    due_date = models.DateField(null=True, blank=True, verbose_name='Fecha de vencimiento')
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de completitud')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_priority_color(self):
        """Retorna color para la prioridad"""
        colors = {
            'low': 'success',
            'medium': 'info',
            'high': 'warning',
            'urgent': 'danger'
        }
        return colors.get(self.priority, 'secondary')
    
    def get_status_color(self):
        """Retorna color para el estado"""
        colors = {
            'todo': 'secondary',
            'in_progress': 'primary',
            'done': 'success'
        }
        return colors.get(self.status, 'secondary')


class TaskComment(models.Model):
    """
    Modelo para comentarios en tareas - US12
    """
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Tarea'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='task_comments',
        verbose_name='Autor'
    )
    content = models.TextField(verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comentario de {self.author.username} en {self.task.title}"


class TaskAttachment(models.Model):
    """
    Modelo para archivos adjuntos en tareas - US13
    """
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='Tarea'
    )
    file = models.FileField(upload_to='task_attachments/', verbose_name='Archivo')
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='uploaded_files',
        verbose_name='Subido por'
    )
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Descripción')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de subida')
    
    class Meta:
        verbose_name = 'Archivo adjunto'
        verbose_name_plural = 'Archivos adjuntos'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.file.name}"
    
    def get_file_extension(self):
        """Obtiene la extensión del archivo"""
        return self.file.name.split('.')[-1].lower() if '.' in self.file.name else ''


class ActivityLog(models.Model):
    """
    Modelo para registrar la actividad del proyecto - US20
    """
    ACTION_CHOICES = [
        ('task_created', 'Tarea Creada'),
        ('task_updated', 'Tarea Actualizada'),
        ('task_assigned', 'Tarea Asignada'),
        ('task_completed', 'Tarea Completada'),
        ('comment_added', 'Comentario Agregado'),
        ('file_uploaded', 'Archivo Subido'),
        ('status_changed', 'Estado Cambiado'),
    ]
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='activity_logs',
        verbose_name='Proyecto'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities',
        verbose_name='Usuario'
    )
    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES,
        verbose_name='Acción'
    )
    description = models.TextField(verbose_name='Descripción')
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='activities',
        verbose_name='Tarea'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    
    class Meta:
        verbose_name = 'Registro de actividad'
        verbose_name_plural = 'Registros de actividad'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()}"
