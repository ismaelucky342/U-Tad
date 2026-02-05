/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 2 - RECIPE CARD                          ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
 * RecipeCard.js - Tarjeta de receta reutilizable
 * 
 * ⚠️ PARA ADAPTAR:
 * - Cambia las propiedades según los datos de tu API
 * - Ajusta los badges/etiquetas según tus categorías
 * - Modifica el diseño según tus necesidades
 */
import React, { useState } from 'react';
import { Card, Badge, Button, Modal } from 'react-bootstrap';
import './RecipeCard.css';

function RecipeCard({ recipe }) {
  const [showModal, setShowModal] = useState(false);

  const handleShow = () => setShowModal(true);
  const handleClose = () => setShowModal(false);

  return (
    <>
      <Card className="recipe-card h-100 shadow-sm">
        <Card.Img 
          variant="top" 
          src={recipe.image} 
          alt={recipe.name}
          className="recipe-image"
        />
        <Card.Body className="d-flex flex-column">
          <Card.Title className="recipe-name mb-3">
            {recipe.name}
          </Card.Title>
          
          <div className="recipe-info mb-3">
            <Badge bg="info" className="me-2">
              📍 {recipe.area}
            </Badge>
            <Badge bg="success">
              🍽️ {recipe.category}
            </Badge>
          </div>

          {recipe.tags && recipe.tags.length > 0 && (
            <div className="recipe-tags mb-3">
              {recipe.tags.slice(0, 2).map((tag, index) => (
                <Badge key={index} bg="secondary" className="me-1 mb-1">
                  {tag}
                </Badge>
              ))}
            </div>
          )}

          <Button 
            variant="primary" 
            className="mt-auto"
            onClick={handleShow}
          >
            Ver Receta 👨‍🍳
          </Button>
        </Card.Body>
      </Card>

      {/* Modal con detalles de la receta */}
      <Modal show={showModal} onHide={handleClose} size="lg">
        <Modal.Header closeButton>
          <Modal.Title>{recipe.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <img 
            src={recipe.image} 
            alt={recipe.name}
            className="img-fluid rounded mb-3"
          />
          
          <div className="mb-3">
            <Badge bg="info" className="me-2">📍 {recipe.area}</Badge>
            <Badge bg="success">🍽️ {recipe.category}</Badge>
          </div>

          {recipe.ingredients && recipe.ingredients.length > 0 && (
            <div className="mb-4">
              <h5>📋 Ingredientes:</h5>
              <ul className="list-group">
                {recipe.ingredients.map((ingredient, index) => (
                  <li key={index} className="list-group-item">
                    {ingredient.measure} {ingredient.name}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {recipe.instructions && (
            <div className="mb-3">
              <h5>👨‍🍳 Instrucciones:</h5>
              <p className="recipe-instructions">{recipe.instructions}</p>
            </div>
          )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cerrar
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default RecipeCard;
