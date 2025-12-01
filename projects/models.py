from django.db import models
from django.conf import settings

class Project(models.Model):
    """
    Modelo para proyectos - US5, US6, US7, US8
    """
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('completed', 'Completado'),
        ('archived', 'Archivado'),
        ('on_hold', 'En Pausa'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Nombre del proyecto')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='created_projects',
        verbose_name='Creador'
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='projects',
        blank=True,
        verbose_name='Miembros'
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='active',
        verbose_name='Estado'
    )
    start_date = models.DateField(null=True, blank=True, verbose_name='Fecha de inicio')
    end_date = models.DateField(null=True, blank=True, verbose_name='Fecha de finalización')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_progress_percentage(self):
        """Calcula el porcentaje de completitud del proyecto - US18"""
        total_tasks = self.tasks.count()
        if total_tasks == 0:
            return 0
        completed_tasks = self.tasks.filter(status='done').count()
        return round((completed_tasks / total_tasks) * 100, 2)
    
    def get_tasks_by_status(self):
        """Obtiene el conteo de tareas por estado - US19"""
        return {
            'todo': self.tasks.filter(status='todo').count(),
            'in_progress': self.tasks.filter(status='in_progress').count(),
            'done': self.tasks.filter(status='done').count(),
        }


class ProjectInvitation(models.Model):
    """
    Modelo para invitaciones a proyectos - US7
    """
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('accepted', 'Aceptada'),
        ('rejected', 'Rechazada'),
    ]
    
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='invitations',
        verbose_name='Proyecto'
    )
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_invitations',
        verbose_name='Invitado por'
    )
    email = models.EmailField(verbose_name='Correo electrónico')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Estado'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de invitación')
    
    class Meta:
        verbose_name = 'Invitación'
        verbose_name_plural = 'Invitaciones'
        ordering = ['-created_at']
        unique_together = ['project', 'email']
    
    def __str__(self):
        return f"{self.project.name} - {self.email}"
