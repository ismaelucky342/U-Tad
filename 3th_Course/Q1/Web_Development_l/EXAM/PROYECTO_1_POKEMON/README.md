# 🔮 Proyecto 1 - Galería de Pokemon

**Plantilla lista para el examen de PWIC**

## 📋 Descripción

Aplicación React con Bootstrap que consume la PokeAPI para mostrar una galería de Pokemon. Diseñada para ser fácilmente modificable en el examen.

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
│   ├── PokemonCard.js   # Tarjeta de Pokemon
│   ├── Navigation.js    # Barra de navegación
│   ├── Footer.js        # Pie de página
│   ├── LoadingSpinner.js # Spinner de carga
│   └── ErrorAlert.js    # Alerta de errores
├── pages/               # Páginas principales
│   ├── LandingPage.js   # Página principal
│   └── SearchPage.js    # Página de búsqueda
├── services/            # Servicios de API
│   └── pokemonAPI.js    # Funciones de API
├── App.js               # Componente principal
└── index.js             # Punto de entrada
```

## ⚠️ Para cambiar de API en el examen

### 1. Modificar `pokemonAPI.js`:
- Cambiar `API_BASE_URL`
- Ajustar endpoints en cada función
- Modificar propiedades de retorno

### 2. Modificar `PokemonCard.js`:
- Cambiar propiedades mostradas
- Ajustar badges/categorías

### 3. Actualizar nombres:
- Renombrar componentes según contexto
- Cambiar textos de UI

## 🎨 Características

- ✅ Diseño responsive con Bootstrap
- ✅ Navegación con React Router
- ✅ Manejo de estados (loading, error)
- ✅ Peticiones asíncronas con Axios
- ✅ Componentes reutilizables
- ✅ Estilos personalizados con CSS

## 📚 APIs alternativas

Puedes cambiar a cualquiera de estas APIs fácilmente:
- RandomUser: https://randomuser.me/api/
- TheMealDB: https://www.themealdb.com/api.php
- Dog CEO: https://dog.ceo/dog-api/
- JSONPlaceholder: https://jsonplaceholder.typicode.com

---

**Ismael Hernandez Clemente** | [GitHub](https://github.com/ismaelucky342)
