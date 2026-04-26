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
const router = express.Router();
const controller = require('../controllers/ordersController');
const validateOrder = require('../middlewares/validateOrder');
const validateId = require('../middlewares/validateId');

// Validar el parámetro `id` antes de procesar rutas que lo llevan
router.param('id', validateId);

// Rutas del endpoint /orders
router.get('/', controller.listOrders);
router.get('/:id', controller.getOrder);
router.post('/', validateOrder, controller.createOrder);
router.put('/:id', validateOrder, controller.updateOrder);
router.delete('/:id', controller.deleteOrder);

module.exports = router;
