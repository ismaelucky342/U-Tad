/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      Examen Final - PW2S                               ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        05/06/2026  -  17:30:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    05/06/2026  -  18:40:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

// src/validators/deliveryValidator.js
const { body } = require('express-validator');

/** Validaciones para crear un nuevo registro meteorológico */
const validatecreateDelivery = [
  body('id_paquete')
    .notEmpty().withMessage('El id de paquete es obligatorio.')
    .optional()
    .isInt({ min: 100000, max: 999999 }).withMessage('Debes insertar un numero de 6 digitos'),
  body('shipment_name')
    .trim()
    .notEmpty().withMessage('El nombre de destinatario es obligatorio.'),
  body('delivery_name')
    .trim()
    .notEmpty().withMessage('El nombre del Emisor es obligatorio.'),

  body('DeliveryDate')
    .optional()
    .isISO8601().withMessage('La fecha debe tener formato ISO 8601'),
];

/** Validaciones para actualizar un registro (todos opcionales) */
const validateupdateDelivery = [
  body('id_paquete')
    .notEmpty().withMessage('El id de paquete es obligatorio.')
    .optional()
    .isInt({ min: 100000, max: 999999 }).withMessage('Debes insertar un numero de 6 digitos'),
 body('shipment_name')
    .trim()
    .notEmpty().withMessage('El nombre de destinatario es obligatorio.'),
  body('delivery_name')
    .trim()
    .notEmpty().withMessage('El nombre del Emisor es obligatorio.'),

  body('DeliveryDate')
    .optional()
    .isISO8601().withMessage('La fecha debe tener formato ISO 8601'),
];

module.exports = { validatecreateDelivery, validateupdateDelivery };
