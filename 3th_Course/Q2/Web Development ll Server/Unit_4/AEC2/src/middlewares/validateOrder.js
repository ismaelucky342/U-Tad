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
  if (!paymentMethod || typeof paymentMethod !== 'string') errors.push('paymentMethod is required and must be a string');
  if (price === undefined || typeof price !== 'number' || price < 0) errors.push('price is required and must be a non-negative number');
  if (!ingredients || typeof ingredients !== 'object' || Array.isArray(ingredients)) errors.push('ingredients is required and must be an object');
  if (errors.length) return res.status(400).json({ success: false, message: 'Validation failed', errors });
  next();
};
