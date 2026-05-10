# 🏍️ EnduroX

Aplicación web desarrollada con **Flask** que permite visualizar, buscar y filtrar un catálogo de motos de competición (motocross y enduro). La interfaz sigue la estética de **KTM**: fondo negro, naranja intenso y tipografía condensada.

---

## 📋 Descripción

MotoExplorer es un proyecto que trabaja con un JSON propio de **32 modelos** de motos off-road de marcas como KTM, Husqvarna, Yamaha, Honda, Kawasaki, Suzuki, Beta, GasGas, Sherco y TM Racing. Cada modelo incluye nombre, marca, tipo, cilindrada, potencia, peso, precio y descripción técnica.

> **Origen de los datos:** JSON elaborado a partir de fichas técnicas públicas de los fabricantes, ampliado y modificado con campos adicionales (potencia en CV, peso en kg, descripción propia).

---

## 🗂️ Estructura del proyecto

```
Proyecto-flask/
├── app.py
├── data/
│   └── motos.json
├── Proyecto Flask 2526.pdf
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── prin.jpg
└── templates/
    ├── 404.html
    ├── base.html
    ├── catalogo.html
    ├── detalle.html
    └── index.html
```

---

## ⚙️ Instalación y ejecución

### 1. Clona o descarga el proyecto

```bash
git clone https://github.com/jfigueroaroldan0/Proyecto-flask.git
cd Proyecto-Flask
```

### 2. Crear entorno virtual

```bash
python -m venv app
source app/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
python3 app.py
```

### 5. Abre en el navegador

```
http://127.0.0.1:5000
```

---

## 🛣️ Rutas de la aplicación

| Ruta | Descripción |
|---|---|
| `/` | Página de inicio con imagen clickable y acceso al catálogo |
| `/motos` | Listado completo con formulario de búsqueda y filtros |
| `/motos?nombre=ktm&marca=KTM&tipo=Motocross&orden=asc` | Ejemplo de búsqueda con parámetros GET |
| `/moto/<id>` | Vista de detalle de un modelo concreto |
| cualquier ruta inválida | Página de error 404 personalizada |

---

## 🔍 Funcionalidades

### Página principal (`/`)
- Logotipo e imagen representativa que enlaza a `/motos`
- Acceso directo a las categorías Motocross y Enduro
- Barra de estadísticas del catálogo (modelos, marcas, cilindradas)

### Búsqueda y listado (`/motos`)
- **Campo de texto** para búsqueda parcial por nombre (no solo por inicio)
- **Selector de marca** generado dinámicamente desde el JSON
- **Filtro por tipo** (Motocross / Enduro) con radio buttons
- **Ordenación** ascendente o descendente por nombre
- Sin filtros → se muestran los 32 modelos
- El formulario **recuerda los valores** tras cada búsqueda (`value`, `selected`)

### Tabla de resultados
- Generada dinámicamente con Jinja2
- Columnas: miniatura, nombre, marca, tipo, cilindrada (cc), potencia (cv), precio y enlace a detalle
- Cada fila es clickable

### Vista de detalle (`/moto/<id>`)
- Muestra toda la información del modelo seleccionado
- Barra visual de potencia relativa respecto al modelo más potente
- Devuelve **error 404** si el identificador no existe
- Enlace de vuelta al listado

---

## 🎨 Diseño

La interfaz imita la estética de **KTM Racing**:

- **Colores:** negro `#0A0A0A` + naranja `#FF6B00`
- **Tipografía:** [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) (display) + Barlow (cuerpo)
- **Elementos visuales:** clip-path angulares en imágenes, franjas diagonales, badges de categoría, sidebar de filtros sticky

---

## 🧱 Plantilla base

`base.html` define la estructura común con dos bloques principales:

```html
{% block title %}...{% endblock %}   <!-- Título de la pestaña -->
{% block content %}...{% endblock %} <!-- Contenido de cada página -->
```

Todas las demás plantillas extienden `base.html` con `{% extends "base.html" %}`.

---

## 📦 Dependencias

| Paquete | Versión mínima |
|---|---|
| Python | 3.9+ |
| Flask | 2.0+ |

No se requieren librerías externas adicionales. El CSS y las fuentes se cargan desde Google Fonts vía CDN.

---

## 📄 Datos del JSON

El archivo `motos.json` contiene un array de objetos con la siguiente estructura:

```json
{
  "id": 1,
  "nombre": "KTM 250 SX-F",
  "marca": "KTM",
  "tipo": "Motocross",
  "cilindrada": 250,
  "potencia_cv": 50,
  "peso_kg": 103.8,
  "precio_euros": 8999,
  "imagen": "https://...",
  "descripcion": "La KTM 250 SX-F es la referencia..."
}
```

**Marcas incluidas:** KTM · Husqvarna · Yamaha · Honda · Kawasaki · Suzuki · Beta · GasGas · Sherco · TM Racing

**Cilindradas:** 125cc — 500cc | **Tipos:** Motocross y Enduro

## 🚀 Despliegue con Railway

La web está alojado en **[Railway](https://railway.com/)**, una plataforma de despliegue en la nube que conecta directamente con GitHub y gestiona toda la infraestructura automáticamente, sin necesidad de configurar servidores.

**🌐 Acceso público:** **[https://motoexplorer-production.up.railway.app/](https://web-production-3003d.up.railway.app/)**

---

### ¿Por qué Railway?

- Sin configuración de servidor ni DevOps
- Integración nativa con GitHub — push y despliega
- Panel de logs en tiempo real
- Dominio HTTPS gratuito incluido
- Plan gratuito suficiente para proyectos académicos

---

### Archivos añadidos para el despliegue

| Archivo | Contenido | Para qué sirve |
|---|---|---|
| `requirements.txt` | `flask` `gunicorn` | Lista de dependencias que Railway instala automáticamente |
| `Procfile` | `web: gunicorn app:app` | Le dice a Railway cómo arrancar la app en producción |

> Railway detecta automáticamente que es una app Python gracias al `requirements.txt`. No hace falta configurar nada más.

---

### Flujo de despliegue

```
Cambio en el código
       ↓
  git push main
       ↓
Railway detecta el push
       ↓
Instala dependencias (requirements.txt)
       ↓
Arranca la app (Procfile → gunicorn)
       ↓
App disponible en la URL pública ✅
```

Cada `git push` a `main` lanza un nuevo despliegue de forma automática, sin intervención manual.

---
