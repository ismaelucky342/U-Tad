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
 * LandingPage.js - Página de inicio
 * 
 * Cargo automáticamente 6 imágenes aleatorias de perros al entrar.
 * Uso useState para el estado y useEffect para cargar al montar.
 */
import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import DogCard from '../components/DogCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getRandomDogs } from '../services/dogAPI';
import './LandingPage.css';

function LandingPage() {
  // Estados para manejar los perros, carga y errores
  const [dogs, setDogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Cargo los perros automáticamente al montar el componente
  useEffect(() => {
    loadDogs();
  }, []); // El array vacío significa "solo al montar"

  const loadDogs = async () => {
    try {
      setLoading(true);
      setError(null);
      const dogsData = await getRandomDogs(6);
      setDogs(dogsData);
    } catch (err) {
      setError(err.message);
      console.error('Error cargando perros:', err);
    } finally {
      setLoading(false);
    }
  };

  // Si está cargando, muestro el spinner
  if (loading) {
    return <LoadingSpinner message="Cargando perros adorables..." />;
  }

  return (
    <div className="landing-page">
      {/* Sección Hero */}
      <section className="hero-section py-5">
        <Container>
          <Row className="align-items-center">
            <Col md={6} className="text-center text-md-start">
              <h1 className="hero-title mb-4">
                🐕 Bienvenido a la Galería de Perros
              </h1>
              <p className="hero-subtitle mb-4">
                Explorá estas fantásticas imágenes aleatorias de perretes.
              </p>
              <Button 
                variant="primary" 
                size="lg"
                onClick={loadDogs}
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

      {/* Alerta de error si hay */}
      {error && <ErrorAlert error={error} onDismiss={() => setError(null)} />}

      {/* Galería de perros */}
      <section className="gallery-section py-5">
        <Container>
          <h2 className="section-title text-center mb-5">
            Perros Aleatorios del Día
          </h2>
          <Row xs={1} md={2} lg={3} className="g-4">
            {dogs.map((dog, index) => (
              <Col key={index}>
                <DogCard imageUrl={dog.imageUrl} breed={dog.breed} />
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
