/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 2 - LANDING PAGE                         ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * Muestra recetas aleatorias y permite recargarlas
 */
import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import RecipeCard from '../components/RecipeCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getRandomRecipes } from '../services/recipeAPI';
import './LandingPage.css';

function LandingPage() {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Cargo recetas al montar el componente
  useEffect(() => {
    loadRecipes();
  }, []);

  const loadRecipes = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getRandomRecipes(6);
      setRecipes(data);
    } catch (err) {
      setError(err.message);
      console.error('Error cargando recetas:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <LoadingSpinner message="Cargando recetas..." />;
  }

  return (
    <div className="landing-page">
      {/* Hero Section */}
      <section className="hero-section text-white text-center py-5">
        <Container>
          <h1 className="hero-title mb-3">👨‍🍳 Galería de Recetas</h1>
          <p className="hero-subtitle mb-4">
            Descubre recetas deliciosas de todo el mundo
          </p>
        </Container>
      </section>

      {/* Error Alert */}
      {error && <ErrorAlert error={error} onDismiss={() => setError(null)} />}

      {/* Recipes Grid */}
      <section className="recipes-section py-5">
        <Container>
          <div className="section-header text-center mb-5">
            <h2 className="section-title">Recetas Aleatorias</h2>
            <p className="section-subtitle">
              Explora nuevas recetas cada vez que recargues
            </p>
          </div>

          <Row xs={1} md={2} lg={3} className="g-4 mb-4">
            {recipes.map((recipe) => (
              <Col key={recipe.id}>
                <RecipeCard recipe={recipe} />
              </Col>
            ))}
          </Row>

          <div className="text-center">
            <Button 
              variant="danger" 
              size="lg"
              onClick={loadRecipes}
              disabled={loading}
            >
              {loading ? 'Cargando...' : '🔄 Cargar Más Recetas'}
            </Button>
          </div>
        </Container>
      </section>
    </div>
  );
}

export default LandingPage;
