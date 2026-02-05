/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 2 - RECIPES API                          ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        05/02/2026  -  XX:XX:XX           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    05/02/2026  -  XX:XX:XX           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

/**
 * recipeAPI.js - Servicio de API para TheMealDB
 * 
 * ⚠️ PARA CAMBIAR A OTRA API:
 * 1. Cambia API_BASE_URL por la URL de tu API
 * 2. Ajusta los endpoints en cada función
 * 3. Modifica las propiedades que devuelves en los return
 * 4. Actualiza los nombres de funciones según tu contexto
 */
import axios from 'axios';

// ⚠️ CAMBIAR: URL base de tu API
const API_BASE_URL = 'https://www.themealdb.com/api/json/v1/1';

/**
 * Función auxiliar para extraer ingredientes
 * TheMealDB tiene formato: strIngredient1, strIngredient2... hasta 20
 */
const extractIngredients = (meal) => {
  const ingredients = [];
  
  for (let i = 1; i <= 20; i++) {
    const ingredient = meal[`strIngredient${i}`];
    const measure = meal[`strMeasure${i}`];
    
    if (ingredient && ingredient.trim() !== '') {
      ingredients.push({
        name: ingredient,
        measure: measure || ''
      });
    }
  }
  
  return ingredients;
};

/**
 * Obtengo una receta aleatoria
 */
export const getRandomRecipe = async () => {
  try {
    // ⚠️ CAMBIAR: Endpoint según tu API
    const response = await axios.get(`${API_BASE_URL}/random.php`);
    const meal = response.data.meals[0];
    
    // ⚠️ CAMBIAR: Propiedades según la respuesta de tu API
    return {
      id: meal.idMeal,
      name: meal.strMeal,
      category: meal.strCategory,
      area: meal.strArea,
      instructions: meal.strInstructions,
      image: meal.strMealThumb,
      tags: meal.strTags ? meal.strTags.split(',') : [],
      ingredients: extractIngredients(meal)
    };
  } catch (error) {
    throw new Error('Error al obtener receta aleatoria');
  }
};

/**
 * Obtengo múltiples recetas aleatorias en paralelo
 */
export const getRandomRecipes = async (count = 6) => {
  try {
    const promises = Array.from({ length: count }, () => getRandomRecipe());
    return await Promise.all(promises);
  } catch (error) {
    throw new Error('Error al obtener múltiples recetas');
  }
};

/**
 * Obtengo todas las categorías disponibles
 */
export const getAllCategories = async () => {
  try {
    // ⚠️ CAMBIAR: Endpoint para obtener categorías
    const response = await axios.get(`${API_BASE_URL}/categories.php`);
    
    return response.data.categories.map(category => ({
      id: category.idCategory,
      name: category.strCategory,
      image: category.strCategoryThumb,
      description: category.strCategoryDescription
    }));
  } catch (error) {
    throw new Error('Error al obtener categorías');
  }
};

/**
 * Obtengo recetas de una categoría específica
 */
export const getRecipesByCategory = async (category, limit = 6) => {
  try {
    // ⚠️ CAMBIAR: Endpoint para filtrar por categoría
    const response = await axios.get(`${API_BASE_URL}/filter.php?c=${category}`);
    
    if (!response.data.meals) {
      return [];
    }
    
    // Limito la cantidad y obtengo los detalles en paralelo
    const mealList = response.data.meals.slice(0, limit);
    const promises = mealList.map(meal => 
      axios.get(`${API_BASE_URL}/lookup.php?i=${meal.idMeal}`)
    );
    const mealDetails = await Promise.all(promises);
    
    return mealDetails.map(detail => {
      const meal = detail.data.meals[0];
      return {
        id: meal.idMeal,
        name: meal.strMeal,
        category: meal.strCategory,
        area: meal.strArea,
        image: meal.strMealThumb,
        tags: meal.strTags ? meal.strTags.split(',') : [],
        ingredients: extractIngredients(meal)
      };
    });
  } catch (error) {
    throw new Error(`Error al obtener recetas de categoría ${category}`);
  }
};

/**
 * Busco recetas por nombre
 */
export const searchRecipeByName = async (searchTerm) => {
  try {
    // ⚠️ CAMBIAR: Endpoint de búsqueda
    const response = await axios.get(`${API_BASE_URL}/search.php?s=${searchTerm}`);
    
    if (!response.data.meals) {
      return [];
    }
    
    return response.data.meals.map(meal => ({
      id: meal.idMeal,
      name: meal.strMeal,
      category: meal.strCategory,
      area: meal.strArea,
      image: meal.strMealThumb,
      instructions: meal.strInstructions,
      tags: meal.strTags ? meal.strTags.split(',') : [],
      ingredients: extractIngredients(meal)
    }));
  } catch (error) {
    throw new Error(`Error al buscar recetas: ${error.message}`);
  }
};

/**
 * Obtengo receta por ID
 */
export const getRecipeById = async (recipeId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/lookup.php?i=${recipeId}`);
    
    if (!response.data.meals) {
      throw new Error('Receta no encontrada');
    }
    
    const meal = response.data.meals[0];
    
    return {
      id: meal.idMeal,
      name: meal.strMeal,
      category: meal.strCategory,
      area: meal.strArea,
      instructions: meal.strInstructions,
      image: meal.strMealThumb,
      tags: meal.strTags ? meal.strTags.split(',') : [],
      ingredients: extractIngredients(meal),
      youtube: meal.strYoutube
    };
  } catch (error) {
    throw new Error(`Error al obtener receta ${recipeId}`);
  }
};
