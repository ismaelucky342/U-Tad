# AEC3 - Migración a React y Bootstrap

## ¿En que ha consistido esta práctica?

Para esta tercera actividad, migré mi galería de perros que hice en la AEC2 (con jQuery y AJAX) a un stack moderno usando **React** y **Bootstrap**. La idea era mantener toda la funcionalidad pero haciéndola más profesional y escalable.

## ¿Qué es React y por qué lo uso?

React es una librería de JavaScript que me permite construir interfaces de usuario dividiéndolas en **componentes reutilizables**. En lugar de manipular el DOM directamente como hacía con jQuery, ahora trabajo con un concepto que React maneja llamado "DOM virtual", que hace todo más rápido y eficiente.

Lo que más me gusta de React:

- **Componentes:** Puedo dividir mi aplicación en piezas pequeñas e independientes
- **Hooks:** `useState` y `useEffect` me permiten manejar el estado y los efectos secundarios de forma muy limpia
- **Declarativo:** Describo cómo quiero que se vea la UI y React se encarga del resto
- **Ecosistema:** Hay miles de librerías que puedo integrar fácilmente

## ¿Qué es Bootstrap y por qué lo uso?

Bootstrap es un framework CSS que me da componentes ya diseñados y un sistema de grid responsive. En lugar de escribir todo el CSS desde cero como en la AEC2, ahora uso componentes de Bootstrap que ya vienen con estilos profesionales y adaptativos.

Ventajas que he notado:

- **Grid System:** Con `Container`, `Row` y `Col` hago layouts responsive sin esfuerzo
- **Componentes listos:** Botones, cards, navbar, forms... todo con clases predefinidas
- **Responsive by default:** No tengo que preocuparme tanto por los media queries
- **React-Bootstrap:** Los componentes nativos de React evitan conflictos con el DOM

## ¿Qué mejora respecto a la AEC2?

La diferencia principal es la **arquitectura**. Antes tenía todo mezclado: HTML, jQuery manipulando el DOM, estilos por todos lados. Ahora tengo:

1. **Código más organizado:** Cada componente tiene su responsabilidad clara
2. **Navegación SPA:** Con React Router cambio de página sin recargar, mucho más fluido
3. **Estado centralizado:** Uso hooks para manejar el estado en lugar de variables globales
4. **Más mantenible:** Si quiero cambiar algo, sé exactamente dónde está
5. **Reutilización:** Los componentes como `DogCard` los uso en varias páginas
6. **Mejor UX:** La app se siente más rápida y moderna

## Estructura que tengo

Organicé todo el código siguiendo una estructura clara:

```
src/
├── App.js                    # Componente principal con el Router
├── index.js                  # Punto de entrada
├── components/               # Componentes reutilizables
│   ├── Navigation.js         # Barra de navegación con enlaces
│   ├── Footer.js             # Pie de página
│   ├── DogCard.js            # Tarjeta individual para cada perro
│   ├── LoadingSpinner.js     # Spinner mientras carga
│   └── ErrorAlert.js         # Alertas de error
├── pages/                    # Las dos páginas principales
│   ├── LandingPage.js        # Inicio con perros aleatorios
│   └── SearchPage.js         # Búsqueda por raza
└── services/                 # Lógica de API separada
    └── dogAPI.js             # Todas las llamadas a la API
```

### ¿Por qué esta estructura?

- **components/**: Todo lo que es reutilizable va aquí. Un componente = un archivo.
- **pages/**: Las "pantallas" principales de la app. Cada ruta del Router renderiza una página.
- **services/**: Separé la lógica de API para no tenerla mezclada con los componentes. Así si cambia la API, solo toco este archivo.

## ¿Cómo funciona todo esto?

### App.js - El corazón de la aplicación

Aquí configuro el Router que maneja la navegación:

```javascript
<Router>
  <Navigation />
  <Routes>
    <Route path="/" element={<LandingPage />} />
    <Route path="/search" element={<SearchPage />} />
  </Routes>
  <Footer />
</Router>
```

### LandingPage - Inicio con perros aleatorios

Cuando cargo la página:
1. `useEffect` se ejecuta automáticamente
2. Llamo a `getRandomDogs(6)` desde dogAPI
3. Guardo las imágenes en el estado con `setDogs`
4. React re-renderiza mostrando las tarjetas

```javascript
useEffect(() => {
  loadDogs();
}, []); // [] significa "solo al montar el componente"
```

### SearchPage - Búsqueda por raza

Similar, pero:
1. Primero cargo todas las razas en el dropdown
2. Cuando selecciono una raza y busco
3. Llamo a `getDogsByBreed(breed, 6)`
4. Muestro los resultados en un grid

### dogAPI.js - Servicio de API

Centralicé todas las llamadas a la API aquí usando Axios:

```javascript
export const getRandomDogs = async (count = 6) => {
  // Hago múltiples llamadas en paralelo con Promise.all
  const promises = Array.from({ length: count }, () => getRandomDog());
  return await Promise.all(promises);
};
```

## Tecnologías que uso

- **React 18:** Para la UI y gestión del estado
- **React Router 6:** Para la navegación entre páginas
- **Axios:** Para las peticiones HTTP (más robusto que fetch)
- **Bootstrap 5 + React-Bootstrap:** Para el diseño y componentes
- **Create React App:** Para la configuración inicial del proyecto


## Extras

Esta migración me ha enseñado mucho sobre cómo estructurar aplicaciones modernas. Pasar de jQuery a React es un cambio de mentalidad: en lugar de decirle al DOM "haz esto", le digo a React "así es como debería verse" y él se encarga del resto.

![Logo U-tad](image.png)
