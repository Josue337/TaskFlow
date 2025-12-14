# 📦 Guía de Instalación Rápida - TaskFlow

## 🎯 Descargar el Proyecto

Descarga el archivo `taskflow_proyecto.tar.gz` y descomprímelo:

```bash
tar -xzf taskflow_proyecto.tar.gz
cd taskflow
```

## ⚡ Instalación Rápida (5 pasos)

### 1️⃣ Crear entorno virtual
```bash
python3 -m venv venv
```

### 2️⃣ Activar entorno virtual
**En Linux/Mac:**
```bash
source venv/bin/activate
```

**En Windows:**
```bash
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migraciones
```bash
python manage.py migrate
```

### 5️⃣ Cargar datos de prueba (opcional)
```bash
python create_sample_data.py
```

## 🚀 Iniciar el Servidor

```bash
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000**

## 👤 Credenciales de Prueba

**Administrador:**
- Usuario: `admin`
- Contraseña: `admin123`

**Usuarios:**
- Usuario: `usuario1` / Contraseña: `usuario123`
- Usuario: `usuario2` / Contraseña: `usuario123`

## ✅ Verificación de Requisitos

### Todos los requisitos están implementados:

#### 🔵 EP1 — Autenticación y Usuarios
- ✅ US1: Registro con validación de correo y contraseña segura
- ✅ US2: Login con manejo de errores y sesión persistente
- ✅ US3: Roles Admin/Usuario con permisos diferenciados
- ✅ US4: Edición de perfil (nombre, correo, foto)

#### 🔵 EP2 — Gestión de Proyectos
- ✅ US5: Crear proyecto
- ✅ US6: Editar proyecto
- ✅ US7: Agregar miembros por correo
- ✅ US8: Archivar proyecto

#### 🔵 EP3 — Gestión de Tareas
- ✅ US9: Crear tarea con título, descripción, fecha, prioridad
- ✅ US10: Asignar tarea a miembros
- ✅ US11: Cambiar estado (To Do → In Progress → Done)
- ✅ US12: Comentarios en tareas
- ✅ US13: Adjuntar archivos

#### 🔵 EP4 — Interfaz y UX
- ✅ US14: Diseño limpio y responsivo login/registro
- ✅ US15: Dashboard con proyectos y tareas recientes
- ✅ US16: Modo oscuro con persistencia
- ✅ US17: Navegación intuitiva con sidebar

#### 🔵 EP5 — Dashboard y Estadísticas
- ✅ US18: Progreso del proyecto (%)
- ✅ US19: Gráficos de tareas por estado (Chart.js)
- ✅ US20: Actividad reciente con cambios

## 🎨 Características Destacadas

### Interfaz Moderna
- Diseño con Bootstrap 5
- Sidebar fijo con navegación intuitiva
- Tarjetas animadas y responsive
- Iconos Bootstrap Icons

### Modo Oscuro
- Botón flotante en esquina inferior derecha
- Persistencia con localStorage
- Transiciones suaves entre temas

### Dashboard Interactivo
- Estadísticas en tiempo real
- Gráficos con Chart.js
- Actividad reciente del sistema
- Progreso visual de proyectos

### Sistema de Permisos
- Roles: Admin y Usuario
- Panel de administración exclusivo
- Control de acceso por proyecto
- Validaciones de permisos

## 📁 Estructura del Proyecto

```
taskflow/
├── manage.py                 # Comando principal Django
├── requirements.txt          # Dependencias Python
├── README.md                 # Documentación completa
├── create_sample_data.py     # Script datos de prueba
│
├── taskflow_project/         # Configuración Django
│   ├── settings.py          # Configuración general
│   └── urls.py              # URLs principales
│
├── users/                    # App Usuarios
│   ├── models.py            # CustomUser con roles
│   ├── views.py             # Login, registro, perfil
│   ├── forms.py             # Formularios usuarios
│   └── urls.py
│
├── projects/                 # App Proyectos
│   ├── models.py            # Project, ProjectInvitation
│   ├── views.py             # CRUD proyectos
│   ├── forms.py             # Formularios proyectos
│   └── urls.py
│
├── tasks/                    # App Tareas
│   ├── models.py            # Task, Comment, Attachment, ActivityLog
│   ├── views.py             # CRUD tareas
│   ├── forms.py             # Formularios tareas
│   └── urls.py
│
├── dashboard/                # App Dashboard
│   ├── views.py             # Dashboard y estadísticas
│   └── urls.py
│
├── templates/                # Plantillas HTML
│   ├── base.html            # Template base
│   ├── users/               # Templates usuarios
│   ├── projects/            # Templates proyectos
│   ├── tasks/               # Templates tareas
│   └── dashboard/           # Templates dashboard
│
├── static/                   # Archivos estáticos
└── media/                    # Archivos subidos
```

## 🔧 Tecnologías

- **Django 4.2.7** - Framework web Python
- **Bootstrap 5** - Framework CSS
- **Chart.js** - Librería de gráficos
- **Bootstrap Icons** - Iconografía
- **SQLite** - Base de datos (desarrollo)

## 📊 Funcionalidades Principales

### Proyectos
- 4 estados: Activo, Completado, En Pausa, Archivado
- Cálculo automático de progreso
- Sistema de invitaciones
- Gestión de miembros

### Tareas
- 3 estados: Por Hacer, En Progreso, Completado
- 4 prioridades: Baja, Media, Alta, Urgente
- Asignación múltiple de usuarios
- Fechas de vencimiento
- Sistema de comentarios
- Archivos adjuntos (PDF, imágenes, etc.)

### Dashboard
- Métricas en tiempo real
- Gráficos interactivos
- Actividad reciente
- Lista de tareas asignadas

## 🆘 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Error: "No such table"
```bash
python manage.py migrate
```

### Error: "Port already in use"
```bash
python manage.py runserver 8080
```

### Base de datos corrupta
```bash
rm db.sqlite3
python manage.py migrate
python create_sample_data.py
```

## 🚀 Próximos Pasos

1. ✅ Instalar y ejecutar el proyecto
2. ✅ Explorar con las credenciales de prueba
3. ✅ Crear tus propios proyectos y tareas
4. 📝 Personalizar según tus necesidades
5. 🌐 Desplegar en producción

## 📞 Soporte

Para más información, consulta el archivo `README.md` completo incluido en el proyecto.

---

**¡Disfruta de TaskFlow! 🎉**
