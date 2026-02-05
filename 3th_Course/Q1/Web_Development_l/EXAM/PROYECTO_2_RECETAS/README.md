# 👨‍🍳 Proyecto 2 - Galería de Recetas

**Plantilla lista para el examen de PWIC**

## 📋 Descripción

Aplicación React con Bootstrap que consume TheMealDB API para mostrar una galería de recetas. Diseñada para ser fácilmente modificable en el examen.

## 🚀 Cómo ejecutar

```bash
# Instalar dependencias
npm install

# Ejecutar en desarrollo
npm start
```

La aplicación se abrirá en `http://localhost:3000`

## 📁 Estructura del proyecto

```
src/
├── components/          # Componentes reutilizables
│   ├── RecipeCard.js    # Tarjeta de receta (con modal)
│   ├── Navigation.js    # Barra de navegación
│   ├── Footer.js        # Pie de página
│   ├── LoadingSpinner.js # Spinner de carga
│   └── ErrorAlert.js    # Alerta de errores
├── pages/               # Páginas principales
│   ├── LandingPage.js   # Página principal
│   └── SearchPage.js    # Página de búsqueda
├── services/            # Servicios de API
│   └── recipeAPI.js     # Funciones de API
├── App.js               # Componente principal
└── index.js             # Punto de entrada
```

## ⚠️ Para cambiar de API en el examen

### 1. Modificar `recipeAPI.js`:
- Cambiar `API_BASE_URL`
- Ajustar endpoints en cada función
- Modificar propiedades de retorno
- Adaptar `extractIngredients()` si es necesario

### 2. Modificar `RecipeCard.js`:
- Cambiar propiedades mostradas
- Ajustar contenido del modal
- Modificar badges/categorías

### 3. Actualizar nombres:
- Renombrar componentes según contexto
- Cambiar textos de UI
- Ajustar estilos de colores

## 🎨 Características

- ✅ Diseño responsive con Bootstrap
- ✅ Modal con detalles de cada receta
- ✅ Navegación con React Router
- ✅ Manejo de estados (loading, error)
- ✅ Peticiones asíncronas con Axios
- ✅ Componentes reutilizables
- ✅ Estilos personalizados con CSS
- ✅ Lista de ingredientes formateada

## 📚 APIs alternativas

Puedes cambiar a cualquiera de estas APIs fácilmente:
- PokeAPI: https://pokeapi.co/
- RandomUser: https://randomuser.me/api/
- Dog CEO: https://dog.ceo/dog-api/
- JSONPlaceholder: https://jsonplaceholder.typicode.com
- CocktailDB: https://www.thecocktaildb.com/api.php

## 💡 Diferencias con Proyecto 1

- **Modal**: RecipeCard tiene un modal con detalles completos
- **Colores**: Esquema rojo/naranja en lugar de púrpura
- **Datos**: Manejo de ingredientes en formato especial
- **API**: TheMealDB en lugar de PokeAPI

---

**Ismael Hernandez Clemente** | [GitHub](https://github.com/ismaelucky342)
