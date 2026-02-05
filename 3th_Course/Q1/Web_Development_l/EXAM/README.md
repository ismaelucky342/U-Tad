# 📚 Plantillas para Examen PWIC

**Ismael Hernandez Clemente** | [GitHub](https://github.com/ismaelucky342)

Este repositorio contiene plantillas React preparadas para el examen de Programación Web en el Cliente (PWIC).

## 📂 Contenido

### 🔮 Proyecto 1 - Galería de Pokemon
- **API**: PokeAPI (https://pokeapi.co/)
- **Colores**: Púrpura/Violeta
- **Características**:
  - Tarjetas de Pokemon con tipos
  - Búsqueda por tipo
  - Datos: altura, peso, habilidades

### 👨‍🍳 Proyecto 2 - Galería de Recetas
- **API**: TheMealDB (https://www.themealdb.com/)
- **Colores**: Rojo/Naranja
- **Características**:
  - Tarjetas con modal de detalles
  - Búsqueda por categoría
  - Lista de ingredientes
  - Instrucciones completas

### 📄 Plantillas JS (Carpeta raíz)
- `PLANTILLA_1_POKEMON.js` - Funciones API Pokemon
- `PLANTILLA_2_USERS.js` - Funciones API Usuarios
- `PLANTILLA_3_MOVIES.js` - Funciones API Películas
- `PLANTILLA_4_RECIPES.js` - Funciones API Recetas

## 🚀 Cómo usar en el examen

### Opción 1: Usar proyecto completo
```bash
cd PROYECTO_1_POKEMON  # o PROYECTO_2_RECETAS
npm install
npm start
```

### Opción 2: Copiar solo el servicio API
1. Copia el archivo del servicio que necesites
2. Modifica las 4 cosas marcadas con ⚠️:
   - URL base de la API
   - Endpoints
   - Propiedades de retorno
   - Nombres de funciones

## ⚠️ 4 cosas a cambiar para adaptar a otra API

### 1️⃣ URL Base
```javascript
const API_BASE_URL = 'https://tu-api.com/v1';
```

### 2️⃣ Endpoints
```javascript
const response = await axios.get(`${API_BASE_URL}/tu-endpoint`);
```

### 3️⃣ Propiedades
```javascript
return {
  id: response.data.id,
  nombre: response.data.nombre,
  // Ajusta según tu API
};
```

### 4️⃣ Nombres
```javascript
export const getTuDato = async () => {
  // Renombra según contexto
};
```

## 📋 Estructura común de los proyectos

```
proyecto/
├── public/
│   └── index.html
├── src/
│   ├── components/      # Componentes reutilizables
│   │   ├── Card.js
│   │   ├── Navigation.js
│   │   ├── Footer.js
│   │   ├── LoadingSpinner.js
│   │   └── ErrorAlert.js
│   ├── pages/          # Páginas
│   │   ├── LandingPage.js
│   │   └── SearchPage.js
│   ├── services/       # APIs
│   │   └── api.js
│   ├── App.js
│   ├── App.css
│   └── index.js
├── package.json
└── README.md
```

## 🎨 Características comunes

- ✅ React 18 + Bootstrap 5
- ✅ React Router para navegación
- ✅ Axios para peticiones HTTP
- ✅ Manejo de estados (loading, error)
- ✅ Diseño responsive
- ✅ Componentes reutilizables
- ✅ Código bien comentado
- ✅ Estilos personalizados

## 📚 APIs gratuitas recomendadas

### Sin API Key
- **PokeAPI**: https://pokeapi.co/
- **TheMealDB**: https://www.themealdb.com/api.php
- **Dog CEO**: https://dog.ceo/dog-api/
- **JSONPlaceholder**: https://jsonplaceholder.typicode.com
- **RandomUser**: https://randomuser.me/
- **Studio Ghibli**: https://ghibliapi.herokuapp.com
- **CocktailDB**: https://www.thecocktaildb.com/api.php

### Con API Key (gratuita)
- **OMDB**: http://www.omdbapi.com/
- **TMDB**: https://www.themoviedb.org/
- **Spoonacular**: https://spoonacular.com/food-api

## 💡 Consejos para el examen

1. **Lee bien el enunciado**: Identifica qué API usar
2. **Copia la plantilla apropiada**: Usa la que más se parezca
3. **Modifica las 4 cosas**: URL, endpoints, propiedades, nombres
4. **Prueba la API primero**: Usa Postman o el navegador
5. **Maneja errores**: Siempre usa try-catch
6. **Comenta tu código**: Explica qué hace cada función

## 🔧 Troubleshooting

### Error de CORS
- Algunas APIs pueden dar error de CORS en desarrollo
- Usa un proxy o la extensión "CORS Unblock"

### Error 404
- Verifica la URL base
- Revisa los endpoints en la documentación de la API
- Comprueba los parámetros requeridos

### Datos undefined
- Console.log la respuesta completa
- Verifica la estructura: response.data.xxx
- Algunas APIs anidan los datos diferente

## 📖 Documentación útil

- [React Docs](https://react.dev/)
- [Bootstrap React](https://react-bootstrap.github.io/)
- [Axios](https://axios-http.com/)
- [React Router](https://reactrouter.com/)

---

**¡Buena suerte en el examen! 🍀**

*Las plantillas están diseñadas para ser modificadas fácilmente. Practica cambiando de API antes del examen.*
