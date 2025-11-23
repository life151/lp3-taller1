# API RESTful de Gestión de Videos 🎥

**Desarrollado por:** Lina Chamorro  
**Proyecto:** Taller 1 — Lenguajes de Programación III  
**Institución:** Uniremington  
**Tecnologías:** Python · Flask · Flask-RESTful · SQLAlchemy · Swagger
Docente:Diego Marin
---

##  Descripción
Accede a la documentación Swagger en http://localhost:5000/apidocs

Esta API RESTful permite gestionar un catálogo de videos, ofreciendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre recursos audiovisuales. Está construida con Flask y documentada con Swagger para facilitar su exploración y pruebas. El proyecto forma parte del Taller 1 de la asignatura Lenguajes de Programación III, con un enfoque educativo y práctico en el desarrollo de servicios web.

---

##  Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/life151/lp3-taller1.git
cd lp3-taller1/lp3-taller1


Esta es una API RESTful para gestión de videos, desarrollada con Flask, Flask-RESTful y SQLAlchemy.

## Descripción

El proyecto implementa una API simple para gestionar información sobre videos, permitiendo:

- Crear nuevos videos
- Consultar videos existentes
- Actualizar información de videos
- Eliminar videos

Cada video tiene los siguientes atributos:
- ID: Identificador único del video
- Nombre: Título del video
- Vistas: Número de reproducciones
- Likes: Número de "me gusta"

## Estructura del Proyecto

```
lp3-taller1
├── app.py                  # Archivo principal para ejecutar la aplicación
├── config.py               # Configuración de la aplicación
├── models/
│   ├── __init__.py         # Inicializa el módulo models
│   └── video.py            # Modelo de datos para Video
├── resources/
│   ├── __init__.py         # Inicializa el módulo resources
│   └── video.py            # Recursos y rutas para Video
├── database.db             # Base de datos SQLite (generada automáticamente)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/UR-CC/lp3-taller1.git
   cd lp3-taller1
   ```

2. Crear un entorno virtual:
   ```
   python -m venv venv
   ```

3. Activar el entorno virtual:
     ```
     source venv/bin/activate
     ```

4. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

1. Iniciar el servidor de desarrollo:
   ```
   python app.py
   ```

2. El servidor estará disponible en `http://localhost:5000`

## Uso de la API

### Obtener un video

```
GET /api/videos/{id}
```

Respuesta:
```json
{
  "id": 1,
  "name": "Tutorial de Python",
  "views": 1500,
  "likes": 120
}
```

### Crear un nuevo video

```
PUT /api/videos/{id}
```

Cuerpo de la solicitud:
```json
{
  "name": "Tutorial de Flask",
  "views": 0,
  "likes": 0
}
```

### Actualizar un video

```
PATCH /api/videos/{id}
```

Cuerpo de la solicitud (campos opcionales):
```json
{
  "views": 2500,
  "likes": 200
}
```

### Eliminar un video

```
DELETE /api/videos/{id}
```

## Desarrollo del Taller

1. Ajustar este `README.md` con los datos del Estudiante

2. Realizar un `commit` por cada ajuste realizando, deben buscar los comentarios `# TODO:`

3. Completar el archivo `app.py`

4. Completar el archivo `resources/video.py`

5. Elaborar un documento con las pruebas realizar para cada método del API REST.

6. Implementar una (1) de las sugerencias que se presentan a continuación.

### Sugerencias de Mejora

1. **Autenticación y autorización**:
   - Implementar JWT para autenticar usuarios
   - Definir roles y permisos

2. **Documentación**:
   - Integrar Swagger/OpenAPI para documentar la API
   - Añadir ejemplos de uso

3. **Validación de datos**:
   - Mejorar la validación de entrada con marshmallow o similar
   - Manejar errores de forma más específica

4. **Funcionalidades adicionales**:
   - Añadir búsqueda y filtrado
   - Implementar paginación
   - Añadir endpoints para obtener todos los videos
   - Implementar sistema de categorías/etiquetas

5. **Migración de Base de datos**:
   - Implementar Flask-Migrate para gestionar cambios en el esquema

6. **Pruebas**:
   - Añadir pruebas unitarias
   - Implementar pruebas de integración
   - Configurar CI/CD

7. **Registro y monitoreo**:
   - Implementar logging
   - Añadir métricas y monitoreo

8. **Despliegue**:
   - Dockerizar la aplicación
   - Configurar para entornos de producción

