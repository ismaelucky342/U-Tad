/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC3 - PWIC                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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

import axios from 'axios';

const API_BASE_URL = 'https://dog.ceo/api';

// Obtener una imagen aleatoria de perro
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

// Obtener múltiples imágenes aleatorias
export const getRandomDogs = async (count = 6) => {
  try {
    const promises = Array.from({ length: count }, () => getRandomDog());
    const results = await Promise.all(promises);
    return results;
  } catch (error) {
    throw new Error('Error al obtener múltiples imágenes');
  }
};

// Obtener todas las razas
export const getAllBreeds = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/breeds/list/all`);
    return Object.keys(response.data.message);
  } catch (error) {
    throw new Error('Error al obtener lista de razas');
  }
};

// Obtener imagen por raza específica
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

// Obtener múltiples imágenes por raza
export const getDogsByBreed = async (breed, count = 6) => {
  try {
    const promises = Array.from({ length: count }, () => getDogByBreed(breed));
    const results = await Promise.all(promises);
    return results;
  } catch (error) {
    throw new Error(`Error al obtener imágenes de la raza ${breed}`);
  }
};
