/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - PW2S                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        17/04/2026  -  01:07:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    17/04/2026  -  12:49:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

const express = require('express');
const ordersRouter = require('./routes/orders');
const errorHandler = require('./middlewares/errorHandler');
const requestLogger = require('./middlewares/logger');

const app = express();

// Leer el cuerpo JSON de las peticiones entrantes
app.use(express.json());

// Registrar cada petición para poder seguir el flujo cuando depuro
app.use(requestLogger);

// Rutas principales de pedidos
app.use('/orders', ordersRouter);

// Respuesta para rutas que no existen
app.use((req, res) => res.status(404).json({ success: false, message: 'Not Found' }));

// Manejador de errores global
app.use(errorHandler);

const PORT = process.env.PORT || 3000;
if (require.main === module) {
  app.listen(PORT, () => console.log(`Server listening on ${PORT}`));
}

module.exports = app;
