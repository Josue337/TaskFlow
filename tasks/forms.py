from django import forms
from .models import Task, TaskComment, TaskAttachment

class TaskForm(forms.ModelForm):
    """Formulario para crear y editar tareas - US9, US10"""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'status', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la tarea',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción detallada de la tarea...'
            }),
            'assigned_to': forms.CheckboxSelectMultiple(),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
    
    def __init__(self, *args, project=None, **kwargs):
        super().__init__(*args, **kwargs)
        if project:
            # Solo mostrar miembros del proyecto para asignar
            self.fields['assigned_to'].queryset = project.members.all()


class TaskCommentForm(forms.ModelForm):
    """Formulario para comentarios en tareas - US12"""
    
    class Meta:
        model = TaskComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe un comentario...',
                'required': True
            })
        }


class TaskAttachmentForm(forms.ModelForm):
    """Formulario para archivos adjuntos - US13"""
    
    class Meta:
        model = TaskAttachment
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del archivo (opcional)'
            })
        }
