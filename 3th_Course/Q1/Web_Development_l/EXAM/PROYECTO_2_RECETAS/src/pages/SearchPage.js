/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 2 - SEARCH PAGE                          ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * Permite buscar recetas por categoría
 */
import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import RecipeCard from '../components/RecipeCard';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorAlert from '../components/ErrorAlert';
import { getAllCategories, getRecipesByCategory } from '../services/recipeAPI';
import './SearchPage.css';

function SearchPage() {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searching, setSearching] = useState(false);
  const [error, setError] = useState(null);

  // Cargo las categorías al montar el componente
  useEffect(() => {
    loadCategories();
  }, []);

  const loadCategories = async () => {
    try {
      setLoading(true);
      setError(null);
      const categoriesList = await getAllCategories();
      setCategories(categoriesList);
      if (categoriesList.length > 0) {
        setSelectedCategory(categoriesList[0].name);
      }
    } catch (err) {
      setError(err.message);
      console.error('Error cargando categorías:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (!selectedCategory) {
      setError('Por favor selecciona una categoría');
      return;
    }

    try {
      setSearching(true);
      setError(null);
      const recipesData = await getRecipesByCategory(selectedCategory, 6);
      setRecipes(recipesData);
    } catch (err) {
      setError(err.message);
      console.error('Error buscando:', err);
    } finally {
      setSearching(false);
    }
  };

  if (loading) {
    return <LoadingSpinner message="Cargando categorías..." />;
  }

  return (
    <div className="search-page">
      {/* Sección de búsqueda */}
      <section className="search-section py-5 bg-light">
        <Container>
          <Row className="justify-content-center">
            <Col md={8}>
              <h1 className="search-title text-center mb-4">
                🔍 Buscar Recetas por Categoría
              </h1>
              <Form onSubmit={handleSearch}>
                <Form.Group className="mb-4">
                  <Form.Label className="fw-bold">Selecciona una categoría:</Form.Label>
                  <Form.Select 
                    value={selectedCategory}
                    onChange={(e) => setSelectedCategory(e.target.value)}
                    size="lg"
                  >
                    {categories.map((category) => (
                      <option key={category.id} value={category.name}>
                        {category.name}
                      </option>
                    ))}
                  </Form.Select>
                </Form.Group>
                <div className="text-center">
                  <Button 
                    variant="danger" 
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
      {recipes.length > 0 && (
        <section className="results-section py-5">
          <Container>
            <h2 className="section-title text-center mb-5">
              Resultados: {selectedCategory}
            </h2>
            <Row xs={1} md={2} lg={3} className="g-4">
              {recipes.map((recipe) => (
                <Col key={recipe.id}>
                  <RecipeCard recipe={recipe} />
                </Col>
              ))}
            </Row>
            <Row className="mt-5">
              <Col className="text-center">
                <Button 
                  variant="outline-danger" 
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
      {!searching && recipes.length === 0 && (
        <Container className="text-center py-5">
          <p className="text-muted fs-5">
            Selecciona una categoría y haz clic en buscar para ver las recetas
          </p>
        </Container>
      )}

      {/* Loading durante búsqueda */}
      {searching && <LoadingSpinner message="Buscando recetas..." />}
    </div>
  );
}

export default SearchPage;
