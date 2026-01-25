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
 * LoadingSpinner.js - Indicador de carga
 * 
 * Muestro este spinner mientras cargo datos de la API.
 * Recibo un mensaje personalizado como prop.
 */
import React from 'react';
import { Spinner, Container, Row, Col } from 'react-bootstrap';

function LoadingSpinner({ message = 'Cargando...' }) {
  return (
    <Container className="py-5">
      <Row className="justify-content-center align-items-center min-vh-50">
        <Col xs={12} className="text-center">
          <Spinner animation="border" role="status" className="mb-3">
            <span className="visually-hidden">Cargando...</span>
          </Spinner>
          <p className="text-muted mt-3">{message}</p>
        </Col>
      </Row>
    </Container>
  );
}

export default LoadingSpinner;
