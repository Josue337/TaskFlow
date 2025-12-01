from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # US1: Registro
    path('register/', views.RegisterView.as_view(), name='register'),
    
    # US2: Login/Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # US4: Perfil
    path('profile/', views.profile_view, name='profile'),
    
    # US3: Panel de administración
    path('admin-panel/', views.admin_panel_view, name='admin_panel'),
    path('change-role/<int:user_id>/', views.change_user_role, name='change_role'),
]
