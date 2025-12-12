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

import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import DogCard from '../components/DogCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getAllBreeds, getDogsByBreed } from '../services/dogAPI';
import './SearchPage.css';

function SearchPage() {
  const [breeds, setBreeds] = useState([]);
  const [selectedBreed, setSelectedBreed] = useState('');
  const [dogs, setDogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searching, setSearching] = useState(false);
  const [error, setError] = useState(null);

  // Cargar lista de razas al montar el componente
  useEffect(() => {
    loadBreeds();
  }, []);

  const loadBreeds = async () => {
    try {
      setLoading(true);
      setError(null);
      const breedsList = await getAllBreeds();
      setBreeds(breedsList);
      if (breedsList.length > 0) {
        setSelectedBreed(breedsList[0]);
      }
    } catch (err) {
      setError(err.message);
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!selectedBreed) {
      setError('Por favor selecciona una raza');
      return;
    }

    try {
      setSearching(true);
      setError(null);
      const dogsData = await getDogsByBreed(selectedBreed, 6);
      setDogs(dogsData);
    } catch (err) {
      setError(err.message);
      console.error('Error:', err);
    } finally {
      setSearching(false);
    }
  };

  const handleDismissError = () => {
    setError(null);
  };

  if (loading) {
    return <LoadingSpinner message="Cargando razas..." />;
  }

  return (
    <div className="search-page">
      {/* Search Section */}
      <section className="search-section py-5 bg-light">
        <Container>
          <Row className="justify-content-center">
            <Col md={8}>
              <h1 className="search-title text-center mb-4">
                🔍 Buscar Perros por Raza
              </h1>
              <Form onSubmit={handleSearch}>
                <Form.Group className="mb-4">
                  <Form.Label className="fw-bold">Selecciona una raza:</Form.Label>
                  <Form.Select 
                    value={selectedBreed}
                    onChange={(e) => setSelectedBreed(e.target.value)}
                    size="lg"
                  >
                    {breeds.map((breed) => (
                      <option key={breed} value={breed}>
                        {breed.charAt(0).toUpperCase() + breed.slice(1)}
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

      {/* Error Alert */}
      {error && (
        <ErrorAlert error={error} onDismiss={handleDismissError} />
      )}

      {/* Results Section */}
      {dogs.length > 0 && (
        <section className="results-section py-5">
          <Container>
            <h2 className="section-title text-center mb-5">
              Resultados de la búsqueda
            </h2>
            <Row xs={1} md={2} lg={3} className="g-4">
              {dogs.map((dog, index) => (
                <Col key={index}>
                  <DogCard 
                    imageUrl={dog.imageUrl}
                    breed={dog.breed}
                    onDownload={() => {}}
                  />
                </Col>
              ))}
            </Row>
            <Row className="mt-5">
              <Col className="text-center">
                <Button 
                  variant="outline-primary" 
                  size="lg"
                  onClick={handleSearch}
                >
                  Buscar más
                </Button>
              </Col>
            </Row>
          </Container>
        </section>
      )}

      {/* No Results Message */}
      {!searching && dogs.length === 0 && !error && (
        <section className="py-5">
          <Container>
            <Row>
              <Col className="text-center">
                <p className="text-muted display-6">
                  Realiza una búsqueda para ver resultados
                </p>
              </Col>
            </Row>
          </Container>
        </section>
      )}

      {searching && <LoadingSpinner message="Buscando perros..." />}
    </div>
  );
}

export default SearchPage;
