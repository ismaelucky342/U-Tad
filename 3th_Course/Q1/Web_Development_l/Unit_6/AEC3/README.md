# Galería de Perros - Migración a React

## Descripción del Proyecto

Este proyecto es una migración de una galería de imágenes de perros de jQuery/AJAX a React con Bootstrap, manteniendo toda la funcionalidad original pero mejorada con:

- React Hooks para gestión de estado
- React Router v6 para navegación entre páginas
- Bootstrap 5 para diseño responsive
- Axios para peticiones a la API
- Componentes reutilizables

## Estructura del Proyecto

```
src/
├── components/
│   ├── Navigation.js         # Navbar con React Router
│   ├── Footer.js             # Footer del sitio
│   ├── DogCard.js            # Componente de tarjeta de perro
│   ├── LoadingSpinner.js     # Spinner de carga
│   └── ErrorAlert.js         # Alerta de errores
├── pages/
│   ├── LandingPage.js        # Página de inicio con perros aleatorios
│   └── SearchPage.js         # Página de búsqueda por raza
├── services/
│   └── dogAPI.js             # Servicios de API con Axios
├── App.js                    # Componente principal con Router
└── index.js                  # Punto de entrada
```

## Instalación y Uso

### 1. Instalar dependencias
```bash
npm install
```

### 2. Ejecutar en modo desarrollo
```bash
npm start
```

La aplicación se abrirá en `http://localhost:3000`

### 3. Compilar para producción
```bash
npm run build
```

## Características Implementadas

### Funcionalidad
- Obtener imágenes aleatorias de perros
- Buscar imágenes por raza específica
- Descargar imágenes
- Manejo de errores con alerts
- Spinner de carga

### Hooks y Estado (React)
- useState para gestionar: dogs, loading, error, selectedBreed
- useEffect para cargar datos al montar componentes
- Custom hooks potenciales para servicios API

### React Router
- Navegación entre Landing Page ("/") y Search Page ("/search")
- Links con react-router-dom
- Navegación sin recargar la página

### Bootstrap
- Navbar responsive con react-bootstrap
- Grid system (Container, Row, Col)
- Componentes: Button, Form, Card, Alert, Spinner
- Clases utility para estilos

### Organización del Código
- Componentes separados y reutilizables
- Servicios API en archivo dedicado
- Estilos modularizados por componente
- Nombres significativos y comentarios

## Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|----------|
| React | 18.2.0 | Framework principal |
| React Router DOM | 6.16.0 | Navegación entre páginas |
| Bootstrap | 5.3.0 | Diseño y componentes UI |
| React Bootstrap | 2.9.0 | Componentes Bootstrap para React |
| Axios | 1.6.0 | Peticiones HTTP |

## API Utilizada

[Dog.ceo API](https://dog.ceo/api) - API pública gratuita para imágenes de perros

### Endpoints principales:
- GET /breeds/image/random - Imagen aleatoria
- GET /breeds/list/all - Lista de todas las razas
- GET /breed/{breed}/images/random - Imagen por raza

## Rutas de la Aplicación

| Ruta | Componente | Descripción |
|------|-----------|-------------|
| / | LandingPage | Página de inicio con perros aleatorios |
| /search | SearchPage | Página de búsqueda por raza |

## Autor

**Ismael Hernández Clemente**
- Email: ismael.hernandez@live.u-tad.com
- GitHub: [ismaelucky342](https://github.com/ismaelucky342)
- Universidad: U-tad

## Año

2025
