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
 * DogCard.js - Tarjeta de perro reutilizable
 * 
 * Componente que muestro en ambas páginas para cada perro.
 * Incluye la imagen, el nombre de la raza y un botón de descarga.
 */
import React from 'react';
import { Card, Button } from 'react-bootstrap';
import './DogCard.css';

function DogCard({ imageUrl, breed }) {
  // Manejo la descarga de la imagen
  const handleDownload = () => {
    const link = document.createElement('a');
    link.href = imageUrl;
    link.download = `dog-${Date.now()}.jpg`;
    link.click();
  };

  return (
    <Card className="dog-card h-100">
      <Card.Img 
        variant="top" 
        src={imageUrl} 
        alt={`Perro de raza ${breed}`}
        className="dog-image"
      />
      <Card.Body className="d-flex flex-column">
        <Card.Title className="text-center">🐕 {breed}</Card.Title>
        <div className="mt-auto">
          <Button 
            variant="primary" 
            size="sm"
            className="w-100"
            onClick={handleDownload}
          >
            Descargar
          </Button>
        </div>
      </Card.Body>
    </Card>
  );
}

export default DogCard;
