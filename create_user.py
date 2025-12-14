import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskflow_project.settings')
django.setup()

from users.models import CustomUser



user3 = CustomUser.objects.create_user(
    username='usuario3',
    email='usuario3@taskflow.com',
    password='usuario123',
    first_name='Cristian',
    last_name='Bello'
)

print(f"✓ Usuarios creados: {user3.username}")
