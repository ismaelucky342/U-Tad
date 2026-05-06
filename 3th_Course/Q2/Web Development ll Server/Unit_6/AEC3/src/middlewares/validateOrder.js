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

module.exports = function validateOrder(req, res, next) {
  const { paymentMethod, price, ingredients } = req.body;
  const errors = [];

  // Validación del campo paymentMethod
  if (!paymentMethod || typeof paymentMethod !== 'string' || !paymentMethod.trim()) {
    errors.push('paymentMethod is required and must be a non-empty string');
  }

  // Validación del campo price
  if (price === undefined || typeof price !== 'number' || Number.isNaN(price) || price < 0) {
    errors.push('price is required and must be a non-negative number');
  }

  // Validación del campo ingredients
  if (ingredients === undefined || ingredients === null || typeof ingredients !== 'object' || Array.isArray(ingredients)) {
    errors.push('ingredients is required and must be an object');
  } else if (Object.keys(ingredients).length === 0) {
    errors.push('ingredients object must include at least one ingredient');
  }

  // Devuelve errores si hay problemas de validación
  if (errors.length) return res.status(400).json({ success: false, message: 'Validation failed', errors });
  next();
};
