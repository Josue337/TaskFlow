from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm

# US1: Registro de usuario
class RegisterView(CreateView):
    """Vista para registro de usuarios"""
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            '¡Cuenta creada exitosamente! Por favor inicia sesión.'
        )
        return response
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:home')
        return super().dispatch(request, *args, **kwargs)


# US2: Inicio de sesión
def login_view(request):
    """Vista para inicio de sesión"""
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.get_full_name_or_username()}!')
            next_url = request.GET.get('next', 'dashboard:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'users/login.html')


# US2: Cerrar sesión
@login_required
def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('users:login')


# US4: Edición de perfil
@login_required
def profile_view(request):
    """Vista para ver y editar perfil"""
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('users:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'users/profile.html', context)


# US3: Panel de administración (solo para admins)
@login_required
def admin_panel_view(request):
    """Vista del panel de administración"""
    if not request.user.is_admin():
        messages.error(request, 'No tienes permisos para acceder al panel de administración.')
        return redirect('dashboard:home')
    
    users = CustomUser.objects.all().order_by('-created_at')
    
    context = {
        'users': users,
        'total_users': users.count(),
        'admin_users': users.filter(role='admin').count(),
        'regular_users': users.filter(role='user').count(),
    }
    return render(request, 'users/admin_panel.html', context)


# US3: Cambiar rol de usuario (solo admins)
@login_required
def change_user_role(request, user_id):
    """Cambiar el rol de un usuario"""
    if not request.user.is_admin():
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('dashboard:home')
    
    try:
        user = CustomUser.objects.get(id=user_id)
        if user.id == request.user.id:
            messages.warning(request, 'No puedes cambiar tu propio rol.')
        else:
            user.role = 'admin' if user.role == 'user' else 'user'
            user.save()
            messages.success(
                request, 
                f'Rol de {user.username} cambiado a {user.get_role_display()}.'
            )
    except CustomUser.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
    
    return redirect('users:admin_panel')
