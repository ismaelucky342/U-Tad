/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC3 - PWIC (React Migration)                     ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        12/12/2025  -  10:30:09           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    16/12/2025  -  01:45:14           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/


/**
 * dogAPI.js - Servicio de API para Dog CEO
 * 
 * Aquí centralizo todas las llamadas a la API de Dog CEO.
 * Uso Axios en lugar de fetch porque maneja mejor los errores
 * y tiene una sintaxis más limpia.
 */
import axios from 'axios';

const API_BASE_URL = 'https://dog.ceo/api';

// Obtengo una imagen aleatoria de perro
export const getRandomDog = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/breeds/image/random`);
    return {
      imageUrl: response.data.message,
      breed: 'Raza Aleatoria'
    };
  } catch (error) {
    throw new Error('Error al obtener imagen de perro aleatorio');
  }
};

// Obtengo múltiples imágenes aleatorias en paralelo
export const getRandomDogs = async (count = 6) => {
  try {
    // Creo un array de promesas y las ejecuto todas a la vez con Promise.all
    const promises = Array.from({ length: count }, () => getRandomDog());
    return await Promise.all(promises);
  } catch (error) {
    throw new Error('Error al obtener múltiples imágenes');
  }
};

// Obtengo todas las razas disponibles de la API
export const getAllBreeds = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/breeds/list/all`);
    return Object.keys(response.data.message);
  } catch (error) {
    throw new Error('Error al obtener lista de razas');
  }
};

// Obtengo una imagen de una raza específica
export const getDogByBreed = async (breed) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/breed/${breed}/images/random`);
    return {
      imageUrl: response.data.message,
      breed: breed.charAt(0).toUpperCase() + breed.slice(1)
    };
  } catch (error) {
    throw new Error(`Error al obtener imagen de la raza ${breed}`);
  }
};

// Obtengo múltiples imágenes de una raza específica
export const getDogsByBreed = async (breed, count = 6) => {
  try {
    const promises = Array.from({ length: count }, () => getDogByBreed(breed));
    return await Promise.all(promises);
  } catch (error) {
    throw new Error(`Error al obtener imágenes de la raza ${breed}`);
  }
};
