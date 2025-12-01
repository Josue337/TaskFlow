"""
Script para crear datos de prueba en TaskFlow
Ejecutar: python manage.py shell < create_sample_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskflow_project.settings')
django.setup()

from users.models import CustomUser
from projects.models import Project
from tasks.models import Task, TaskComment

# Crear usuarios
print("Creando usuarios...")
admin_user = CustomUser.objects.create_user(
    username='admin',
    email='admin@taskflow.com',
    password='admin123',
    role='admin',
    first_name='Administrador',
    last_name='Sistema'
)

user1 = CustomUser.objects.create_user(
    username='usuario1',
    email='usuario1@taskflow.com',
    password='usuario123',
    first_name='Juan',
    last_name='Pérez'
)

user2 = CustomUser.objects.create_user(
    username='usuario2',
    email='usuario2@taskflow.com',
    password='usuario123',
    first_name='María',
    last_name='García'
)

print(f"✓ Usuarios creados: {admin_user.username}, {user1.username}, {user2.username}")

# Crear proyectos
print("\nCreando proyectos...")
project1 = Project.objects.create(
    name='Desarrollo Web',
    description='Proyecto de desarrollo de aplicación web con Django',
    creator=admin_user,
    status='active'
)
project1.members.add(admin_user, user1, user2)

project2 = Project.objects.create(
    name='App Móvil',
    description='Aplicación móvil para gestión de tareas',
    creator=user1,
    status='in_progress'
)
project2.members.add(user1, user2)

project3 = Project.objects.create(
    name='Marketing Digital',
    description='Campaña de marketing en redes sociales',
    creator=user2,
    status='active'
)
project3.members.add(user2, admin_user)

print(f"✓ Proyectos creados: {project1.name}, {project2.name}, {project3.name}")

# Crear tareas
print("\nCreando tareas...")
task1 = Task.objects.create(
    title='Diseñar base de datos',
    description='Crear el esquema de la base de datos del proyecto',
    project=project1,
    created_by=admin_user,
    status='done',
    priority='high'
)
task1.assigned_to.add(user1)

task2 = Task.objects.create(
    title='Implementar autenticación',
    description='Sistema de login y registro de usuarios',
    project=project1,
    created_by=admin_user,
    status='in_progress',
    priority='urgent'
)
task2.assigned_to.add(user1, user2)

task3 = Task.objects.create(
    title='Diseño de interfaz',
    description='Crear mockups de la interfaz de usuario',
    project=project1,
    created_by=user1,
    status='todo',
    priority='medium'
)
task3.assigned_to.add(user2)

task4 = Task.objects.create(
    title='Testing de aplicación',
    description='Realizar pruebas de la aplicación móvil',
    project=project2,
    created_by=user1,
    status='todo',
    priority='high'
)
task4.assigned_to.add(user2)

task5 = Task.objects.create(
    title='Crear contenido para redes',
    description='Generar posts para Instagram y Facebook',
    project=project3,
    created_by=user2,
    status='in_progress',
    priority='medium'
)
task5.assigned_to.add(admin_user)

print(f"✓ Tareas creadas: 5 tareas en total")

# Crear comentarios
print("\nCreando comentarios...")
TaskComment.objects.create(
    task=task2,
    author=user1,
    content='He comenzado con la implementación del login'
)

TaskComment.objects.create(
    task=task2,
    author=user2,
    content='Necesitamos revisar los requisitos de seguridad'
)

print("✓ Comentarios agregados")

print("\n" + "="*50)
print("DATOS DE PRUEBA CREADOS EXITOSAMENTE")
print("="*50)
print("\nCredenciales de acceso:")
print("\nAdministrador:")
print("  Usuario: admin")
print("  Password: admin123")
print("\nUsuarios normales:")
print("  Usuario: usuario1 / Password: usuario123")
print("  Usuario: usuario2 / Password: usuario123")
print("\n" + "="*50)
