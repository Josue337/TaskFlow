from django import forms
from .models import Project, ProjectInvitation

class ProjectForm(forms.ModelForm):
    """Formulario para crear y editar proyectos - US5, US6"""
    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del proyecto',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del proyecto...'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class ProjectInvitationForm(forms.ModelForm):
    """Formulario para invitar miembros - US7"""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com',
            'required': True
        }),
        help_text='Introduce el correo electrónico del usuario a invitar'
    )
    
    class Meta:
        model = ProjectInvitation
        fields = ['email']
