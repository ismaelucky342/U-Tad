/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 1 - POKEMON CARD                         ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * PokemonCard.js - Tarjeta de Pokemon reutilizable
 * 
 * ⚠️ PARA ADAPTAR:
 * - Cambia las propiedades según los datos de tu API
 * - Ajusta los badges/etiquetas según tus categorías
 * - Modifica el diseño según tus necesidades
 */
import React from 'react';
import { Card, Badge } from 'react-bootstrap';
import './PokemonCard.css';

function PokemonCard({ pokemon }) {
  // Colores para cada tipo de Pokemon
  const typeColors = {
    normal: '#A8A878',
    fire: '#F08030',
    water: '#6890F0',
    electric: '#F8D030',
    grass: '#78C850',
    ice: '#98D8D8',
    fighting: '#C03028',
    poison: '#A040A0',
    ground: '#E0C068',
    flying: '#A890F0',
    psychic: '#F85888',
    bug: '#A8B820',
    rock: '#B8A038',
    ghost: '#705898',
    dragon: '#7038F8',
    dark: '#705848',
    steel: '#B8B8D0',
    fairy: '#EE99AC'
  };

  return (
    <Card className="pokemon-card h-100 shadow-sm">
      <div className="pokemon-card-header">
        <span className="pokemon-id">#{String(pokemon.id).padStart(3, '0')}</span>
      </div>
      <Card.Img 
        variant="top" 
        src={pokemon.imageUrl} 
        alt={pokemon.name}
        className="pokemon-image"
      />
      <Card.Body className="d-flex flex-column">
        <Card.Title className="text-center mb-3 pokemon-name">
          {pokemon.name}
        </Card.Title>
        
        <div className="pokemon-types text-center mb-3">
          {pokemon.types.map((type, index) => (
            <Badge 
              key={index}
              className="me-1"
              style={{ 
                backgroundColor: typeColors[type] || '#777',
                color: 'white'
              }}
            >
              {type}
            </Badge>
          ))}
        </div>

        <div className="pokemon-info mt-auto">
          <div className="info-row">
            <span className="info-label">Altura:</span>
            <span className="info-value">{(pokemon.height / 10).toFixed(1)} m</span>
          </div>
          <div className="info-row">
            <span className="info-label">Peso:</span>
            <span className="info-value">{(pokemon.weight / 10).toFixed(1)} kg</span>
          </div>
        </div>
      </Card.Body>
    </Card>
  );
}

export default PokemonCard;
