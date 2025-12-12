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
import { Container, Row, Col, Button } from 'react-bootstrap';
import DogCard from '../components/DogCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getRandomDogs } from '../services/dogAPI';
import './LandingPage.css';

function LandingPage() {
  const [dogs, setDogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Cargar perros al montar el componente
  useEffect(() => {
    loadDogs();
  }, []);

  const loadDogs = async () => {
    try {
      setLoading(true);
      setError(null);
      const dogsData = await getRandomDogs(6);
      setDogs(dogsData);
    } catch (err) {
      setError(err.message);
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDismissError = () => {
    setError(null);
  };

  if (loading) {
    return <LoadingSpinner message="Cargando perros adorables..." />;
  }

  return (
    <div className="landing-page">
      {/* Hero Section */}
      <section className="hero-section py-5">
        <Container>
          <Row className="align-items-center">
            <Col md={6} className="text-center text-md-start">
              <h1 className="hero-title mb-4">
                🐕 Bienvenido a la Galería de Perros
              </h1>
              <p className="hero-subtitle mb-4">
                Exploremos juntas estas fantásticas imágenes aleatorias de perretes.
              </p>
              <Button 
                variant="primary" 
                size="lg"
                onClick={loadDogs}
                className="me-3"
              >
                Recargar Perros
              </Button>
            </Col>
            <Col md={6} className="text-center">
              <p className="display-1">🐶</p>
            </Col>
          </Row>
        </Container>
      </section>

      {/* Error Alert */}
      {error && (
        <ErrorAlert error={error} onDismiss={handleDismissError} />
      )}

      {/* Dogs Gallery */}
      <section className="gallery-section py-5">
        <Container>
          <h2 className="section-title text-center mb-5">
            Perros Aleatorios del Día
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
                onClick={loadDogs}
              >
                Cargar más perros
              </Button>
            </Col>
          </Row>
        </Container>
      </section>
    </div>
  );
}

export default LandingPage;
