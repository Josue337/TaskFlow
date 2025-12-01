from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # US9: Crear tarea
    path('project/<int:project_pk>/create/', views.task_create, name='create'),
    
    # Detalle de tarea (US12, US13)
    path('<int:pk>/', views.task_detail, name='detail'),
    
    # US9, US10: Editar tarea
    path('<int:pk>/update/', views.task_update, name='update'),
    
    # US11: Cambiar estado
    path('<int:pk>/change-status/', views.task_change_status, name='change_status'),
    
    # Eliminar tarea
    path('<int:pk>/delete/', views.task_delete, name='delete'),
    
    # Eliminar comentario
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    
    # Eliminar archivo adjunto
    path('attachment/<int:pk>/delete/', views.attachment_delete, name='attachment_delete'),
]
