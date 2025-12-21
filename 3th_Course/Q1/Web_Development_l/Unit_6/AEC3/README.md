# AEC3 - Migración de Galería de Perros a React con Bootstrap

## Introducción

La AEC2 original consistía en una galería de imágenes de perros desarrollada con tecnologías tradicionales web (HTML, CSS y JavaScript con jQuery), mientras que esta AEC3 representa la evolución hacia una aplicación React con Bootstrap.

El proyecto mantiene la funcionalidad core de la galería de perros, pero introduce mejoras significativas en términos de arquitectura, mantenibilidad y experiencia de usuario. La migración no solo implica un cambio tecnológico, sino también una reestructuración completa del código para aprovechar las ventajas de los componentes reutilizables y el estado reactivo.

## Objetivos del Proyecto

Los objetivos principales de esta migración fueron:

- **Modernizar la tecnología:** Migrar de jQuery/AJAX a React Hooks y Axios
- **Mejorar la arquitectura:** Implementar componentes reutilizables y separación clara de responsabilidades
- **Optimizar la experiencia de usuario:** Introducir navegación SPA con React Router
- **Mantener funcionalidad:** Preservar todas las características de la AEC2 original
- **Responsive design:** Utilizar Bootstrap para un diseño adaptativo mejorado
- **Mejorar el rendimiento:** Implementar lazy loading y gestión eficiente del estado

## Análisis de la AEC2 Original

La AEC2 era una aplicación web tradicional que utilizaba:

- **HTML/CSS/JavaScript puro** con jQuery para manipulación del DOM
- **Peticiones AJAX** directas con jQuery para consumir la API de Dog CEO
- **Estructura monolítica** con archivos separados para estilos y scripts
- **Navegación tradicional** con enlaces que recargaban la página completa

### Fortalezas de la AEC2:
- Funcionalidad completa según requisitos
- Diseño responsive básico
- Validación de formularios implementada
- Manejo de errores adecuado

### Limitaciones identificadas:
- Código procedural difícil de mantener
- Manipulación directa del DOM propensa a errores
- Estado disperso en variables globales
- Navegación que recarga la página completa
- Dificultad para reutilizar componentes

## Diseño y Arquitectura

### Arquitectura de Componentes

La nueva arquitectura se basa en el patrón de componentes de React:

```
src/
├── components/          # Componentes reutilizables
│   ├── Navigation.js    # Barra de navegación con React Router
│   ├── Footer.js        # Pie de página
│   ├── DogCard.js       # Tarjeta individual de perro
│   ├── LoadingSpinner.js # Indicador de carga
│   └── ErrorAlert.js    # Componente de alertas de error
├── pages/              # Páginas principales (rutas)
│   ├── LandingPage.js  # Página de inicio
│   └── SearchPage.js   # Página de búsqueda
├── services/           # Servicios externos
│   └── dogAPI.js       # Cliente API con Axios
├── App.js              # Componente raíz con Router
└── index.js            # Punto de entrada
```

### Gestión del Estado

Se implementó una gestión de estado local utilizando React Hooks:

- **useState** para estado de componentes individuales
- **useEffect** para efectos secundarios (carga de datos)
- Estado centralizado en componentes padre cuando necesario

### Navegación SPA

Se implementó React Router v6 para navegación sin recarga:

- Rutas declarativas con `<Routes>` y `<Route>`
- Navegación programática con `useNavigate`
- Links activos con `NavLink`

## Implementación Técnica

### Configuración del Proyecto

Se inició el proyecto con Create React App para una configuración rápida y estándar:

```bash
npx create-react-app aec3-dog-gallery
cd aec3-dog-gallery
npm install react-router-dom axios bootstrap react-bootstrap
```

### Componentes Principales

#### Navigation Component
```javascript
// Implementación básica del navbar responsive
import { Navbar, Nav, Container } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const Navigation = () => (
  <Navbar bg="primary" expand="lg">
    <Container>
      <LinkContainer to="/">
        <Navbar.Brand>Galería de Perros</Navbar.Brand>
      </LinkContainer>
      <Nav className="me-auto">
        <LinkContainer to="/">
          <Nav.Link>Inicio</Nav.Link>
        </LinkContainer>
        <LinkContainer to="/search">
          <Nav.Link>Búsqueda</Nav.Link>
        </LinkContainer>
      </Nav>
    </Container>
  </Navbar>
);
```

#### Landing Page
La página de inicio carga automáticamente 5 imágenes aleatorias al montar el componente:

```javascript
useEffect(() => {
  loadRandomDogs();
}, []);

const loadRandomDogs = async () => {
  setLoading(true);
  try {
    const response = await dogAPI.getRandomDogs(5);
    setDogs(response.data.message);
  } catch (error) {
    setError('Error al cargar imágenes');
  } finally {
    setLoading(false);
  }
};
```

#### Search Page
Implementa un formulario con validación y búsqueda por raza:

- Dropdown dinámico de razas cargado desde la API
- Campo numérico con validación de rango
- Manejo de sub-razas cuando existen
- Resultados mostrados en grid responsive

### Servicios API

Se centralizó la lógica de API en un módulo dedicado:

```javascript
// dogAPI.js
import axios from 'axios';

const API_BASE = 'https://dog.ceo/api';

export const getRandomDogs = (count) => 
  axios.get(`${API_BASE}/breeds/image/random/${count}`);

export const getBreeds = () => 
  axios.get(`${API_BASE}/breeds/list/all`);

export const getDogsByBreed = (breed, count) => 
  axios.get(`${API_BASE}/breed/${breed}/images/random/${count}`);
```

## Tecnologías Utilizadas

| Tecnología | Versión | Justificación |
|------------|---------|---------------|
| **React** | 18.2.0 | Framework moderno para UI componentes |
| **React Router DOM** | 6.16.0 | Navegación SPA sin recarga |
| **Bootstrap** | 5.3.0 | Framework CSS responsive |
| **React Bootstrap** | 2.9.0 | Componentes Bootstrap nativos para React |
| **Axios** | 1.6.0 | Cliente HTTP más robusto que fetch |

### Justificación de Elecciones Tecnológicas

- **React sobre Vue/Angular:** Mayor adopción en la industria y mejor integración con herramientas existentes
- **React Router sobre alternativas:** Estándar de facto para React
- **Bootstrap sobre CSS puro:** Acelera desarrollo y garantiza responsive design
- **Axios sobre fetch:** Mejor manejo de errores y soporte para interceptores

## Funcionalidades Implementadas

### Funcionalidades Core
- ✅ Carga automática de imágenes aleatorias en landing page
- ✅ Búsqueda por raza con formulario completo
- ✅ Manejo de sub-razas dinámico
- ✅ Validación de formularios con feedback visual
- ✅ Manejo de errores con alertas Bootstrap
- ✅ Estados de carga con spinners

### Mejoras sobre AEC2
- 🔄 Navegación SPA sin recargas
- 📱 Diseño más responsive con Bootstrap Grid
- ♻️ Componentes reutilizables
- ⚡ Mejor rendimiento con React
- 🎨 UI más moderna y consistente

## Pruebas y Validación

### Pruebas Funcionales
- Verificación de carga de imágenes aleatorias
- Validación de formulario de búsqueda
- Prueba de navegación entre rutas
- Test de manejo de errores de red

### Pruebas de Responsive Design
- Desktop (>1024px): Grid de 4 columnas
- Tablet (768-1024px): Grid de 3 columnas  
- Mobile (<768px): Grid de 2 columnas

### Validación de API
- Manejo de respuestas exitosas
- Gestión de errores HTTP
- Validación de datos recibidos

## Dificultades y Soluciones

### Migración de jQuery a React
**Problema:** La manipulación directa del DOM con jQuery no se traduce directamente a React.

**Solución:** Reestructuración completa pensando en estado y props. Los event listeners se convirtieron en manejadores de eventos de React.

### Gestión del Estado Asíncrono
**Problema:** Coordinar loading states y errores en operaciones asíncronas.

**Solución:** Implementación de patrón consistente con useState para loading/error y useEffect para efectos secundarios.

### Integración Bootstrap con React
**Problema:** Conflictos entre clases CSS de Bootstrap y estilos de componentes.

**Solución:** Uso de React Bootstrap para componentes nativos, evitando manipulación directa de clases CSS.

## Conclusiones

Esta migración ha demostrado las ventajas significativas de los frameworks modernos de frontend:

### Logros Alcanzados
- ✅ Migración completa manteniendo toda funcionalidad
- ✅ Mejora sustancial en mantenibilidad del código
- ✅ Experiencia de usuario superior con SPA
- ✅ Diseño más robusto y responsive

### Aprendizajes Obtenidos
- Arquitectura de componentes y reutilización
- Gestión de estado en aplicaciones React
- Integración de librerías externas
- Mejores prácticas de desarrollo frontend moderno

### Recomendaciones Futuras
- Implementar testing automatizado con Jest/React Testing Library
- Añadir TypeScript para mayor robustez
- Considerar state management global (Redux/Zustand) para aplicaciones más complejas
- Implementar PWA features para mejor UX offline

Esta actividad ha sido fundamental para comprender la evolución de las tecnologías web y la importancia de elegir las herramientas adecuadas para cada proyecto.

## Bibliografía

- [Documentación Oficial de React](https://react.dev/)
- [React Router Documentation](https://reactrouter.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Dog CEO API](https://dog.ceo/dog-api/)
- [React Bootstrap](https://react-bootstrap.github.io/)

---

**Ismael Hernández Clemente**  
*Desarrollo Web I - U-tad*  
Diciembre 2025
