from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser
    US1, US2, US3, US4
    """
    ROLE_CHOICES = [
        ('user', 'Usuario'),
        ('admin', 'Administrador'),
    ]
    
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='user',
        verbose_name='Rol'
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True,
        verbose_name='Foto de perfil'
    )
    bio = models.TextField(blank=True, null=True, verbose_name='Biografía')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.username
    
    def is_admin(self):
        """Verifica si el usuario es administrador"""
        return self.role == 'admin'
    
    def get_full_name_or_username(self):
        """Retorna el nombre completo o username si no existe"""
        full_name = super().get_full_name()
        return full_name if full_name else self.username
