/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      PROYECTO 1 - FOOTER                               ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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

import React from 'react';
import { Container } from 'react-bootstrap';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer bg-dark text-white mt-5 py-4">
      <Container className="text-center">
        <p className="mb-2">🔮 Pokemon Gallery - Examen PWIC</p>
        <p className="mb-0 text-muted">
          Ismael Hernandez Clemente | 
          <a href="https://github.com/ismaelucky342" target="_blank" rel="noopener noreferrer" className="text-white ms-1">
            GitHub
          </a>
        </p>
      </Container>
    </footer>
  );
}

export default Footer;
