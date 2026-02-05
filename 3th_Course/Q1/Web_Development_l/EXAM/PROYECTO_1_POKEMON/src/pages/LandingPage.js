/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 1 - LANDING PAGE                         ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * LandingPage.js - Página principal
 * 
 * Muestra Pokemon aleatorios y permite recargarlos
 */
import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import PokemonCard from '../components/PokemonCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getRandomPokemons } from '../services/pokemonAPI';
import './LandingPage.css';

function LandingPage() {
  const [pokemons, setPokemons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Cargo Pokemon al montar el componente
  useEffect(() => {
    loadPokemons();
  }, []);

  const loadPokemons = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getRandomPokemons(6);
      setPokemons(data);
    } catch (err) {
      setError(err.message);
      console.error('Error cargando Pokemon:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <LoadingSpinner message="Cargando Pokemon..." />;
  }

  return (
    <div className="landing-page">
      {/* Hero Section */}
      <section className="hero-section text-white text-center py-5">
        <Container>
          <h1 className="hero-title mb-3">🔮 Galería de Pokemon</h1>
          <p className="hero-subtitle mb-4">
            Descubre Pokemon aleatorios o busca tus favoritos
          </p>
        </Container>
      </section>

      {/* Error Alert */}
      {error && <ErrorAlert error={error} onDismiss={() => setError(null)} />}

      {/* Pokemon Grid */}
      <section className="pokemon-section py-5">
        <Container>
          <div className="section-header text-center mb-5">
            <h2 className="section-title">Pokemon Aleatorios</h2>
            <p className="section-subtitle">
              Descubre nuevos Pokemon cada vez que recargues
            </p>
          </div>

          <Row xs={1} md={2} lg={3} className="g-4 mb-4">
            {pokemons.map((pokemon) => (
              <Col key={pokemon.id}>
                <PokemonCard pokemon={pokemon} />
              </Col>
            ))}
          </Row>

          <div className="text-center">
            <Button 
              variant="primary" 
              size="lg"
              onClick={loadPokemons}
              disabled={loading}
            >
              {loading ? 'Cargando...' : '🔄 Cargar Más Pokemon'}
            </Button>
          </div>
        </Container>
      </section>
    </div>
  );
}

export default LandingPage;
