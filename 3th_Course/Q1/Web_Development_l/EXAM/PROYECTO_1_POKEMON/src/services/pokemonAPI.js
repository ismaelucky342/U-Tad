/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 1 - POKEMON API                          ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * pokemonAPI.js - Servicio de API para Pokemon
 * 
 * ⚠️ PARA CAMBIAR A OTRA API:
 * 1. Cambia API_BASE_URL por la URL de tu API
 * 2. Ajusta los endpoints en cada función
 * 3. Modifica las propiedades que devuelves en los return
 * 4. Actualiza los nombres de funciones según tu contexto
 */
import axios from 'axios';

// ⚠️ CAMBIAR: URL base de tu API
const API_BASE_URL = 'https://pokeapi.co/api/v2';

/**
 * Obtengo un Pokemon aleatorio (del 1 al 898)
 */
export const getRandomPokemon = async () => {
  try {
    const randomId = Math.floor(Math.random() * 898) + 1;
    
    // ⚠️ CAMBIAR: Endpoint según tu API
    const response = await axios.get(`${API_BASE_URL}/pokemon/${randomId}`);
    
    // ⚠️ CAMBIAR: Propiedades según la respuesta de tu API
    return {
      id: response.data.id,
      name: response.data.name.charAt(0).toUpperCase() + response.data.name.slice(1),
      imageUrl: response.data.sprites.other['official-artwork'].front_default || response.data.sprites.front_default,
      types: response.data.types.map(type => type.type.name),
      weight: response.data.weight,
      height: response.data.height,
      abilities: response.data.abilities.map(ability => ability.ability.name)
    };
  } catch (error) {
    throw new Error('Error al obtener Pokemon aleatorio');
  }
};

/**
 * Obtengo múltiples Pokemon aleatorios en paralelo
 */
export const getRandomPokemons = async (count = 6) => {
  try {
    const promises = Array.from({ length: count }, () => getRandomPokemon());
    return await Promise.all(promises);
  } catch (error) {
    throw new Error('Error al obtener múltiples Pokemon');
  }
};

/**
 * Obtengo lista de tipos de Pokemon disponibles
 */
export const getAllTypes = async () => {
  try {
    // ⚠️ CAMBIAR: Endpoint para obtener categorías/tipos
    const response = await axios.get(`${API_BASE_URL}/type`);
    return response.data.results.map(type => type.name);
  } catch (error) {
    throw new Error('Error al obtener tipos de Pokemon');
  }
};

/**
 * Obtengo Pokemon de un tipo específico
 */
export const getPokemonsByType = async (type, limit = 6) => {
  try {
    // ⚠️ CAMBIAR: Endpoint para filtrar por tipo/categoría
    const response = await axios.get(`${API_BASE_URL}/type/${type}`);
    
    // Limito la cantidad y obtengo los detalles en paralelo
    const pokemonList = response.data.pokemon.slice(0, limit);
    const promises = pokemonList.map(p => axios.get(p.pokemon.url));
    const pokemonDetails = await Promise.all(promises);
    
    return pokemonDetails.map(detail => ({
      id: detail.data.id,
      name: detail.data.name.charAt(0).toUpperCase() + detail.data.name.slice(1),
      imageUrl: detail.data.sprites.other['official-artwork'].front_default || detail.data.sprites.front_default,
      types: detail.data.types.map(t => t.type.name),
      weight: detail.data.weight,
      height: detail.data.height
    }));
  } catch (error) {
    throw new Error(`Error al obtener Pokemon de tipo ${type}`);
  }
};

/**
 * Busco Pokemon por nombre
 */
export const searchPokemonByName = async (name) => {
  try {
    // ⚠️ CAMBIAR: Endpoint de búsqueda
    const response = await axios.get(`${API_BASE_URL}/pokemon/${name.toLowerCase()}`);
    
    return {
      id: response.data.id,
      name: response.data.name.charAt(0).toUpperCase() + response.data.name.slice(1),
      imageUrl: response.data.sprites.other['official-artwork'].front_default || response.data.sprites.front_default,
      types: response.data.types.map(type => type.type.name),
      weight: response.data.weight,
      height: response.data.height,
      abilities: response.data.abilities.map(ability => ability.ability.name),
      stats: response.data.stats.map(stat => ({
        name: stat.stat.name,
        value: stat.base_stat
      }))
    };
  } catch (error) {
    throw new Error(`No se encontró el Pokemon "${name}"`);
  }
};
