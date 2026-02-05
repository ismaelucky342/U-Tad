/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 1 - SEARCH PAGE                          ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * SearchPage.js - Página de búsqueda
 * 
 * Permite buscar Pokemon por tipo
 */
import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import PokemonCard from '../components/PokemonCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getAllTypes, getPokemonsByType } from '../services/pokemonAPI';
import './SearchPage.css';

function SearchPage() {
  const [types, setTypes] = useState([]);
  const [selectedType, setSelectedType] = useState('');
  const [pokemons, setPokemons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searching, setSearching] = useState(false);
  const [error, setError] = useState(null);

  // Cargo los tipos al montar el componente
  useEffect(() => {
    loadTypes();
  }, []);

  const loadTypes = async () => {
    try {
      setLoading(true);
      setError(null);
      const typesList = await getAllTypes();
      setTypes(typesList);
      if (typesList.length > 0) {
        setSelectedType(typesList[0]);
      }
    } catch (err) {
      setError(err.message);
      console.error('Error cargando tipos:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (!selectedType) {
      setError('Por favor selecciona un tipo');
      return;
    }

    try {
      setSearching(true);
      setError(null);
      const pokemonData = await getPokemonsByType(selectedType, 6);
      setPokemons(pokemonData);
    } catch (err) {
      setError(err.message);
      console.error('Error buscando:', err);
    } finally {
      setSearching(false);
    }
  };

  if (loading) {
    return <LoadingSpinner message="Cargando tipos..." />;
  }

  return (
    <div className="search-page">
      {/* Sección de búsqueda */}
      <section className="search-section py-5 bg-light">
        <Container>
          <Row className="justify-content-center">
            <Col md={8}>
              <h1 className="search-title text-center mb-4">
                🔍 Buscar Pokemon por Tipo
              </h1>
              <Form onSubmit={handleSearch}>
                <Form.Group className="mb-4">
                  <Form.Label className="fw-bold">Selecciona un tipo:</Form.Label>
                  <Form.Select 
                    value={selectedType}
                    onChange={(e) => setSelectedType(e.target.value)}
                    size="lg"
                  >
                    {types.map((type) => (
                      <option key={type} value={type}>
                        {type.charAt(0).toUpperCase() + type.slice(1)}
                      </option>
                    ))}
                  </Form.Select>
                </Form.Group>
                <div className="text-center">
                  <Button 
                    variant="primary" 
                    size="lg"
                    type="submit"
                    disabled={searching}
                  >
                    {searching ? 'Buscando...' : 'Buscar'}
                  </Button>
                </div>
              </Form>
            </Col>
          </Row>
        </Container>
      </section>

      {/* Alerta de error */}
      {error && <ErrorAlert error={error} onDismiss={() => setError(null)} />}

      {/* Resultados de la búsqueda */}
      {pokemons.length > 0 && (
        <section className="results-section py-5">
          <Container>
            <h2 className="section-title text-center mb-5">
              Resultados: Tipo {selectedType.charAt(0).toUpperCase() + selectedType.slice(1)}
            </h2>
            <Row xs={1} md={2} lg={3} className="g-4">
              {pokemons.map((pokemon) => (
                <Col key={pokemon.id}>
                  <PokemonCard pokemon={pokemon} />
                </Col>
              ))}
            </Row>
            <Row className="mt-5">
              <Col className="text-center">
                <Button 
                  variant="outline-primary" 
                  size="lg"
                  onClick={handleSearch}
                  disabled={searching}
                >
                  {searching ? 'Buscando...' : '🔄 Buscar Más'}
                </Button>
              </Col>
            </Row>
          </Container>
        </section>
      )}

      {/* Mensaje si aún no hay búsqueda */}
      {!searching && pokemons.length === 0 && (
        <Container className="text-center py-5">
          <p className="text-muted fs-5">
            Selecciona un tipo y haz clic en buscar para ver los Pokemon
          </p>
        </Container>
      )}

      {/* Loading durante búsqueda */}
      {searching && <LoadingSpinner message="Buscando Pokemon..." />}
    </div>
  );
}

export default SearchPage;
