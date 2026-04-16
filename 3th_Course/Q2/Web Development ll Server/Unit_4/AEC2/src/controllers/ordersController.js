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

const data = require('../data/ordersData');

function listOrders(req, res) {
  res.json({ success: true, data: data.orders });
}

function getOrder(req, res) {
  const id = parseInt(req.params.id, 10);
  const order = data.orders.find(o => o.id === id);
  if (!order) return res.status(404).json({ success: false, message: 'Order not found' });
  res.json({ success: true, data: order });
}

function createOrder(req, res) {
  const { paymentMethod, price, ingredients } = req.body;
  const newOrder = {
    id: data.nextId++,
    orderNumber: data.nextOrderNumber++,
    paymentMethod,
    price,
    ingredients
  };
  data.orders.push(newOrder);
  res.status(201).json({ success: true, data: newOrder });
}

function updateOrder(req, res) {
  const id = parseInt(req.params.id, 10);
  const idx = data.orders.findIndex(o => o.id === id);
  if (idx === -1) return res.status(404).json({ success: false, message: 'Order not found' });
  const { paymentMethod, price, ingredients } = req.body;
  const updated = Object.assign(data.orders[idx], { paymentMethod, price, ingredients });
  res.json({ success: true, data: updated });
}

function deleteOrder(req, res) {
  const id = parseInt(req.params.id, 10);
  const idx = data.orders.findIndex(o => o.id === id);
  if (idx === -1) return res.status(404).json({ success: false, message: 'Order not found' });
  const removed = data.orders.splice(idx, 1)[0];
  res.json({ success: true, data: removed });
}

module.exports = { listOrders, getOrder, createOrder, updateOrder, deleteOrder };
