# 🧪 Instrucciones de Prueba - TaskFlow

## 🎯 Cómo Probar Todas las Funcionalidades

Este documento te guía paso a paso para probar **todas las 20 historias de usuario** implementadas.

---

## 🚀 Inicio Rápido

1. **Instalar** siguiendo `GUIA_INSTALACION.md`
2. **Cargar datos de prueba:**
   ```bash
   python create_sample_data.py
   ```
3. **Iniciar servidor:**
   ```bash
   python manage.py runserver
   ```
4. **Abrir navegador:** http://127.0.0.1:8000

---

## 🔵 EP1 — Autenticación y Usuarios

### ✅ US1: Registro de Usuario

**Pasos:**
1. Ve a http://127.0.0.1:8000/users/register/
2. Completa el formulario:
   - Usuario: `testuser`
   - Email: `test@example.com`
   - Contraseña: `test123456` (mínimo 8 caracteres)
   - Confirmar contraseña: `test123456`
3. Click en "Crear Cuenta"

**Resultado esperado:**
- ✅ Mensaje de confirmación
- ✅ Redirección a página de login
- ✅ Validación de email único
- ✅ Validación de contraseña segura

### ✅ US2: Inicio de Sesión

**Pasos:**
1. Ve a http://127.0.0.1:8000/users/login/
2. Ingresa credenciales:
   - Usuario: `admin`
   - Contraseña: `admin123`
3. Click en "Iniciar Sesión"

**Resultado esperado:**
- ✅ Mensaje de bienvenida
- ✅ Redirección al dashboard
- ✅ Sesión persistente (permanece logueado)
- ✅ Mensaje de error si credenciales incorrectas

### ✅ US3: Roles de Usuario (Admin/Usuario)

**Pasos:**
1. Login como `admin` / `admin123`
2. Ve a http://127.0.0.1:8000/users/admin-panel/
3. Observa la lista de usuarios
4. Click en "Cambiar Rol" de un usuario
5. Cierra sesión y login como `usuario1` / `usuario123`
6. Intenta acceder a `/users/admin-panel/`

**Resultado esperado:**
- ✅ Admin puede acceder al panel
- ✅ Admin puede cambiar roles
- ✅ Usuario normal NO puede acceder al panel
- ✅ Mensaje de error de permisos

### ✅ US4: Edición de Perfil

**Pasos:**
1. Login como cualquier usuario
2. Click en "Mi Perfil" en el sidebar
3. Edita:
   - Nombre: `Test`
   - Apellido: `User`
   - Email: `nuevo@email.com`
   - Biografía: `Soy un usuario de prueba`
   - Subir foto de perfil
4. Click en "Guardar Cambios"

**Resultado esperado:**
- ✅ Perfil actualizado
- ✅ Mensaje de confirmación
- ✅ Foto visible en sidebar
- ✅ Cambios guardados en la base de datos

---

## 🔵 EP2 — Gestión de Proyectos

### ✅ US5: Crear Proyecto

**Pasos:**
1. Click en "Proyectos" en sidebar
2. Click en "Nuevo Proyecto"
3. Completa:
   - Nombre: `Proyecto de Prueba`
   - Descripción: `Este es un proyecto de prueba`
   - Estado: `Activo`
   - Fecha inicio: `2024-01-01`
4. Click en "Crear Proyecto"

**Resultado esperado:**
- ✅ Proyecto creado
- ✅ Usuario es automáticamente miembro
- ✅ Redirección a detalle del proyecto
- ✅ Proyecto visible en lista

### ✅ US6: Editar Información del Proyecto

**Pasos:**
1. Ve al detalle de un proyecto
2. Click en botón de editar (icono lápiz)
3. Cambia:
   - Nombre: `Proyecto Editado`
   - Estado: `En Pausa`
4. Click en "Actualizar Proyecto"

**Resultado esperado:**
- ✅ Proyecto actualizado
- ✅ Cambios visibles en detalle
- ✅ Solo creador/admin puede editar

### ✅ US7: Agregar Miembros al Proyecto

**Pasos:**
1. Ve al detalle de un proyecto
2. Click en "Invitar" (botón azul)
3. Ingresa email de usuario existente: `usuario2@taskflow.com`
4. Click en "Enviar Invitación"
5. Prueba con email no registrado: `nuevo@usuario.com`

**Resultado esperado:**
- ✅ Usuario existente agregado inmediatamente
- ✅ Email no registrado crea invitación pendiente
- ✅ Mensaje de confirmación
- ✅ Miembro aparece en lista de miembros

### ✅ US8: Archivar Proyecto

**Pasos:**
1. Ve al detalle de un proyecto
2. Click en "Archivar" (botón gris)
3. Ve a "Proyectos Archivados" en sidebar
4. Click en "Desarchivar"

**Resultado esperado:**
- ✅ Proyecto archivado no aparece en lista principal
- ✅ Proyecto visible en sección archivados
- ✅ Se puede desarchivar
- ✅ Solo creador/admin puede archivar

---

## 🔵 EP3 — Gestión de Tareas

### ✅ US9: Crear Tarea

**Pasos:**
1. Ve al detalle de un proyecto
2. Click en "Nueva Tarea"
3. Completa:
   - Título: `Tarea de Prueba`
   - Descripción: `Descripción detallada`
   - Estado: `Por Hacer`
   - Prioridad: `Alta`
   - Fecha vencimiento: `2024-12-31`
4. Click en "Guardar"

**Resultado esperado:**
- ✅ Tarea creada
- ✅ Visible en lista de tareas del proyecto
- ✅ Todos los campos guardados correctamente

### ✅ US10: Asignar Tarea

**Pasos:**
1. Al crear/editar tarea
2. Selecciona uno o más miembros en "Asignar a"
3. Guarda la tarea
4. Ve al dashboard del usuario asignado

**Resultado esperado:**
- ✅ Tarea aparece en dashboard del asignado
- ✅ Múltiples usuarios pueden ser asignados
- ✅ Solo miembros del proyecto aparecen en lista

### ✅ US11: Cambiar Estado de la Tarea

**Pasos:**
1. Ve al detalle de una tarea
2. En "Cambiar estado" selecciona:
   - `En Progreso`
3. Observa el cambio automático
4. Cambia a `Completado`

**Resultado esperado:**
- ✅ Estado cambia inmediatamente
- ✅ Badge de color actualizado
- ✅ Progreso del proyecto actualizado
- ✅ Registro en actividad

### ✅ US12: Comentarios en las Tareas

**Pasos:**
1. Ve al detalle de una tarea
2. En sección "Comentarios" escribe:
   - `Este es un comentario de prueba`
3. Click en "Comentar"
4. Agrega otro comentario
5. Intenta eliminar un comentario

**Resultado esperado:**
- ✅ Comentario publicado instantáneamente
- ✅ Muestra autor y fecha
- ✅ Comentarios ordenados cronológicamente
- ✅ Solo autor/admin puede eliminar

### ✅ US13: Adjuntar Archivos

**Pasos:**
1. Ve al detalle de una tarea
2. En sección "Archivos Adjuntos"
3. Selecciona un archivo (PDF, imagen, etc.)
4. Agrega descripción opcional
5. Click en "Subir"
6. Click en el archivo para descargarlo

**Resultado esperado:**
- ✅ Archivo subido correctamente
- ✅ Aparece en lista con icono
- ✅ Se puede descargar
- ✅ Solo autor/admin puede eliminar

---

## 🔵 EP4 — Interfaz y Experiencia de Usuario

### ✅ US14: Diseño del Login/Registro

**Pruebas visuales:**
1. Abre `/users/login/` y `/users/register/`
2. Observa:
   - Diseño limpio con gradientes
   - Iconos en campos de formulario
   - Animaciones al cargar
3. Prueba en móvil (F12 → responsive mode)

**Resultado esperado:**
- ✅ Diseño moderno y limpio
- ✅ Gradientes y sombras
- ✅ Responsive en móvil
- ✅ Iconos Bootstrap Icons

### ✅ US15: Dashboard Principal

**Pasos:**
1. Login y ve al dashboard (página principal)
2. Observa:
   - Tarjetas de estadísticas (4 métricas)
   - Gráficos de tareas
   - Lista de tareas recientes
   - Actividad reciente
   - Mis proyectos

**Resultado esperado:**
- ✅ Dashboard con información en tiempo real
- ✅ Estadísticas visuales
- ✅ Acceso rápido a proyectos y tareas

### ✅ US16: Modo Oscuro

**Pasos:**
1. Click en botón flotante (esquina inferior derecha)
2. Observa el cambio de tema
3. Recarga la página
4. Click nuevamente para volver al tema claro

**Resultado esperado:**
- ✅ Cambio instantáneo de tema
- ✅ Persistencia al recargar
- ✅ Transiciones suaves
- ✅ Icono cambia (luna/sol)

### ✅ US17: Navegación Intuitiva

**Pruebas:**
1. Observa el sidebar fijo
2. Navega por diferentes secciones
3. Observa el indicador de página activa
4. Prueba en móvil (menú hamburguesa)

**Resultado esperado:**
- ✅ Sidebar fijo y siempre visible
- ✅ Íconos claros para cada sección
- ✅ Página activa resaltada
- ✅ Responsive en móvil

---

## 🔵 EP5 — Dashboard y Estadísticas

### ✅ US18: Progreso del Proyecto

**Pasos:**
1. Ve al detalle de un proyecto con tareas
2. Observa la barra de progreso
3. Completa una tarea
4. Observa el cambio de porcentaje

**Resultado esperado:**
- ✅ Porcentaje calculado automáticamente
- ✅ Barra visual de progreso
- ✅ Actualización al completar tareas

### ✅ US19: Gráficos de Tareas por Estado

**Pasos:**
1. Ve al Dashboard principal
2. Observa los dos gráficos:
   - Tareas por Estado (gráfico de dona)
   - Tareas por Prioridad (gráfico de barras)
3. Ve a `/statistics/` para más gráficos

**Resultado esperado:**
- ✅ Gráficos interactivos con Chart.js
- ✅ Colores diferenciados por estado
- ✅ Datos en tiempo real
- ✅ Responsive

### ✅ US20: Actividad Reciente

**Pasos:**
1. Ve al Dashboard
2. Observa sección "Actividad Reciente"
3. Realiza acciones:
   - Crear tarea
   - Cambiar estado
   - Agregar comentario
4. Actualiza el dashboard

**Resultado esperado:**
- ✅ Feed de actividad actualizado
- ✅ Muestra usuario, acción y fecha
- ✅ Ordenado cronológicamente
- ✅ Avatar de usuario visible

---

## 🎯 Checklist de Pruebas Completas

### Autenticación
- [ ] Registro con validaciones
- [ ] Login con manejo de errores
- [ ] Roles funcionando
- [ ] Edición de perfil

### Proyectos
- [ ] Crear proyecto
- [ ] Editar proyecto
- [ ] Invitar miembros
- [ ] Archivar proyecto

### Tareas
- [ ] Crear tarea
- [ ] Asignar tarea
- [ ] Cambiar estados
- [ ] Agregar comentarios
- [ ] Adjuntar archivos

### Interfaz
- [ ] Diseño limpio login/registro
- [ ] Dashboard funcional
- [ ] Modo oscuro con persistencia
- [ ] Navegación intuitiva

### Estadísticas
- [ ] Progreso de proyectos
- [ ] Gráficos interactivos
- [ ] Actividad reciente

---

## 🐛 Reporte de Problemas

Si encuentras algún problema, verifica:

1. ✅ Migraciones aplicadas: `python manage.py migrate`
2. ✅ Datos de prueba cargados: `python create_sample_data.py`
3. ✅ Servidor corriendo: `python manage.py runserver`
4. ✅ Permisos correctos del usuario

---

## ✨ Funcionalidades Adicionales

El proyecto incluye funcionalidades extra:

- 🔒 Validaciones de permisos en todos los niveles
- 📧 Sistema de invitaciones por email
- 📊 Métricas en tiempo real
- 🎨 Animaciones y transiciones suaves
- 📱 Diseño completamente responsive
- 🔔 Registro de actividad completo
- 🗂️ Filtros en listas de proyectos
- 🔍 Búsqueda y ordenamiento

---

**¡Disfruta probando TaskFlow! 🚀**
