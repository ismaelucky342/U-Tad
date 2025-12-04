# Galería de Perros - U-tad

Proyecto de galería de imágenes de perros que consume la API de Dog CEO.

## Descripción

Este proyecto implementa una aplicación web frontend compuesta por dos páginas:

1. Landing Page (index.html): Muestra 5 imágenes aleatorias de perros al cargar la página
2. Página de Búsqueda (search.html): Permite buscar imágenes de perros por raza y sub-raza

## Características

- Diseño responsive y flex siguiendo los estilos de U-tad
- Navegación entre páginas mediante navbar
- Carga dinámica de imágenes desde la API
- Dropdown de razas cargado automáticamente desde la API
- Dropdown de sub-razas que se actualiza según la raza seleccionada
- Control de razas sin sub-razas
- Validación de formularios
- Manejo de errores en la UI
- Control de imágenes duplicadas
- Uso de jQuery para manipulación del DOM

## Estructura del Proyecto

```
AEC2/
├── index.html          # Landing page
├── search.html         # Página de búsqueda
├── styles.css          # Archivo principal de estilos (importa módulos)
├── script.js           # JavaScript para landing page
├── search.js           # JavaScript para página de búsqueda
├── image.png           # Logo de U-tad
├── css/                # Módulos CSS separados
│   ├── variables.css   # Variables CSS y reset
│   ├── navbar.css      # Estilos de navegación
│   ├── layout.css      # Estructura y layout general
│   ├── gallery.css     # Estilos de galería de imágenes
│   ├── forms.css       # Estilos de formularios
│   └── responsive.css  # Media queries
└── README.md           # Este archivo
```

## Tecnologías Utilizadas

- HTML5
- CSS3 (Flexbox, CSS Variables)
- JavaScript (ES6+)
- jQuery 3.6.0
- Dog CEO API

## Uso

### Instalación

1. Clona o descarga este repositorio
2. Abre index.html en tu navegador web

No se requiere instalación de dependencias ya que jQuery se carga desde CDN.

### Navegación

- Inicio: Muestra 5 imágenes aleatorias de perros
- Búsqueda: Permite buscar imágenes por raza específica

### Búsqueda de Imágenes

1. Selecciona una raza del dropdown
2. Si la raza tiene sub-razas, selecciona una (opcional)
3. Introduce la cantidad de imágenes que deseas (1-50)
4. Haz clic en "Buscar Imágenes"

## Estilos U-tad

El diseño utiliza la paleta de colores corporativa:
- Color primario: #0066cc (Azul U-tad)
- Color secundario: #004999 (Azul oscuro)
- Color de acento: #ff6b35 (Naranja)

## Manejo de Errores

El sistema controla los siguientes casos de error:
- Conexión a internet fallida
- Respuestas inválidas de la API
- Razas o sub-razas no encontradas
- Formularios incompletos
- Cantidades de imágenes inválidas
- Imágenes que no cargan correctamente

Todos los errores se muestran en la interfaz de usuario con mensajes claros.

## API Endpoints Utilizados

- GET /breeds/list/all - Lista todas las razas y sub-razas
- GET /breeds/image/random/{count} - Obtiene imágenes aleatorias
- GET /breed/{breed}/images - Obtiene todas las imágenes de una raza
- GET /breed/{breed}/{subbreed}/images - Obtiene imágenes de una sub-raza

## Responsive Design

La aplicación es completamente responsive con breakpoints en:
- Desktop: > 1024px
- Tablet: 768px - 1024px
- Mobile: < 768px
- Mobile pequeño: < 480px

## Autor

[Tu Nombre Aquí]  
Desarrollo Web I - U-tad  
2025

## Licencia

Este proyecto es parte de una actividad académica de U-tad.

## Referencias

- Dog CEO API Documentation: https://dog.ceo/dog-api/documentation/
- jQuery Documentation: https://api.jquery.com/
- MDN Web Docs: https://developer.mozilla.org/
