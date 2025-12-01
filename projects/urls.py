from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # US5: Crear proyecto
    path('create/', views.project_create, name='create'),
    
    # Lista de proyectos
    path('', views.project_list, name='list'),
    
    # Detalle del proyecto (US18, US19, US20)
    path('<int:pk>/', views.project_detail, name='detail'),
    
    # US6: Editar proyecto
    path('<int:pk>/update/', views.project_update, name='update'),
    
    # US8: Archivar proyecto
    path('<int:pk>/archive/', views.project_archive, name='archive'),
    
    # US7: Invitar miembros
    path('<int:pk>/invite/', views.project_invite, name='invite'),
    
    # Proyectos archivados
    path('archived/', views.project_archived_list, name='archived'),
]
