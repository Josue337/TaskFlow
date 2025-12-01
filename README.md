# 🚀 TaskFlow - Sistema de Gestión de Tareas y Proyectos

Sistema completo de gestión de tareas y proyectos desarrollado en Django que implementa todas las historias de usuario especificadas.

## ✨ Características Principales

### 🔵 EP1 — Autenticación y Usuarios
- ✅ **US1**: Registro de usuario con validación de correo y contraseña segura
- ✅ **US2**: Inicio de sesión con manejo de errores y sesión persistente
- ✅ **US3**: Sistema de roles (Admin/Usuario) con permisos diferenciados
- ✅ **US4**: Edición de perfil (nombre, correo, foto)

### 🔵 EP2 — Gestión de Proyectos
- ✅ **US5**: Crear proyectos con nombre y creador
- ✅ **US6**: Editar información del proyecto
- ✅ **US7**: Agregar miembros al proyecto por correo
- ✅ **US8**: Archivar/desarchivar proyectos

### 🔵 EP3 — Gestión de Tareas
- ✅ **US9**: Crear tareas con título, descripción, fecha y prioridad
- ✅ **US10**: Asignar tareas a miembros del proyecto
- ✅ **US11**: Cambiar estado de tareas (To Do → In Progress → Done)
- ✅ **US12**: Sistema de comentarios en tareas
- ✅ **US13**: Adjuntar archivos (PDF, imágenes, etc.)

### 🔵 EP4 — Interfaz y Experiencia de Usuario
- ✅ **US14**: Diseño limpio y responsivo para login/registro
- ✅ **US15**: Dashboard principal con proyectos y tareas recientes
- ✅ **US16**: Modo oscuro con persistencia
- ✅ **US17**: Navegación intuitiva con sidebar

### 🔵 EP5 — Dashboard y Estadísticas
- ✅ **US18**: Progreso del proyecto (porcentaje de completitud)
- ✅ **US19**: Gráficos de tareas por estado y prioridad
- ✅ **US20**: Actividad reciente con cambios y comentarios

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, Chart.js
- **Base de datos**: SQLite (desarrollo)
- **Formularios**: Django Crispy Forms
- **Iconos**: Bootstrap Icons

## 📦 Instalación

### 1. Clonar el repositorio o descomprimir
```bash
cd taskflow
```

### 2. Crear y activar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 6. Cargar datos de prueba (opcional)
```bash
python manage.py shell < create_sample_data.py
```

### 7. Iniciar el servidor
```bash
python manage.py runserver
```

Accede a: **http://127.0.0.1:8000**

## 👥 Credenciales de Prueba

Si cargaste los datos de prueba:

**Administrador:**
- Usuario: `admin`
- Contraseña: `admin123`

**Usuarios normales:**
- Usuario: `usuario1` / Contraseña: `usuario123`
- Usuario: `usuario2` / Contraseña: `usuario123`

## 📁 Estructura del Proyecto

```
taskflow/
├── manage.py
├── requirements.txt
├── README.md
├── create_sample_data.py
├── taskflow_project/        # Configuración principal
│   ├── settings.py
│   └── urls.py
├── users/                   # App de usuarios
│   ├── models.py           # CustomUser con roles
│   ├── views.py            # Login, registro, perfil
│   ├── forms.py
│   └── admin.py
├── projects/                # App de proyectos
│   ├── models.py           # Project, ProjectInvitation
│   ├── views.py            # CRUD de proyectos
│   ├── forms.py
│   └── admin.py
├── tasks/                   # App de tareas
│   ├── models.py           # Task, Comment, Attachment, ActivityLog
│   ├── views.py            # CRUD de tareas
│   ├── forms.py
│   └── admin.py
├── dashboard/               # App de dashboard
│   ├── views.py            # Dashboard y estadísticas
│   └── urls.py
├── templates/               # Plantillas HTML
│   ├── base.html           # Template base con sidebar
│   ├── users/
│   ├── projects/
│   ├── tasks/
│   └── dashboard/
├── static/                  # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
└── media/                   # Archivos subidos
    ├── profile_pics/
    └── task_attachments/
```

## 🎨 Características de la Interfaz

### Modo Oscuro (US16)
- Botón flotante en la esquina inferior derecha
- Persistencia con localStorage
- Transiciones suaves

### Navegación (US17)
- Sidebar fijo con iconos
- Responsive para móviles
- Indicador de página activa
- Información del usuario

### Dashboard (US15)
- Tarjetas de estadísticas rápidas
- Gráficos interactivos con Chart.js
- Lista de tareas recientes
- Actividad del sistema

### Gráficos (US19)
- Tareas por estado (gráfico de dona)
- Tareas por prioridad (gráfico de barras)
- Proyectos por estado (gráfico circular)

## 🔐 Sistema de Permisos

### Administradores (Admin)
- Acceso al panel de administración
- Cambiar roles de usuarios
- Editar/eliminar cualquier proyecto o tarea
- Ver todos los proyectos

### Usuarios Normales (User)
- Crear proyectos propios
- Invitar miembros a sus proyectos
- Crear y gestionar tareas en proyectos donde son miembros
- Ver solo proyectos donde son miembros

## 📊 Funcionalidades Clave

### Proyectos
- Estados: Activo, Completado, En Pausa, Archivado
- Cálculo automático de progreso
- Invitaciones por correo
- Gestión de miembros

### Tareas
- Estados: Por Hacer, En Progreso, Completado
- Prioridades: Baja, Media, Alta, Urgente
- Asignación múltiple
- Fechas de vencimiento
- Sistema de comentarios
- Archivos adjuntos

### Actividad
- Registro automático de cambios
- Historial por proyecto
- Notificaciones visuales

## 🚀 Despliegue en Producción

Para producción, modifica `settings.py`:

1. **Cambiar SECRET_KEY**
2. **DEBUG = False**
3. **ALLOWED_HOSTS = ['tudominio.com']**
4. **Configurar base de datos PostgreSQL**
5. **Configurar servidor de archivos estáticos**
6. **Configurar email real (SMTP)**

## 📝 Licencia

Proyecto educativo - Libre uso

## 👨‍💻 Autor

Desarrollado con Django y ❤️

---

## 🆘 Soporte

Para problemas o sugerencias, revisar la documentación de Django o contactar al desarrollador.

**¡Disfruta gestionando tus proyectos con TaskFlow! 🎉**
