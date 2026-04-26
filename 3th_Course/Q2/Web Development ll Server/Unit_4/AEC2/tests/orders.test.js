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

const request = require('supertest');
const app = require('../src/index');
const data = require('../src/data/ordersData');

const initialOrders = [
  {
    id: 1,
    orderNumber: 1001,
    paymentMethod: 'card',
    price: 9.99,
    ingredients: { bun: 'sesame', patty: 'beef', cheese: true }
  }
];

describe('Orders API', () => {
  let createdId;

  beforeEach(() => {
    data.orders.splice(0, data.orders.length, ...initialOrders.map(order => ({
      ...order,
      ingredients: { ...order.ingredients }
    })));
    data.nextId = 2;
    data.nextOrderNumber = 1002;
  });

  test('GET /orders returns success and array', async () => {
    const res = await request(app).get('/orders');

    expect(res.statusCode).toBe(200);
    expect(res.body).toEqual(expect.objectContaining({ success: true }));
    expect(Array.isArray(res.body.data)).toBe(true);
    expect(res.body.data.length).toBeGreaterThanOrEqual(1);
  });

  test('POST /orders should create a valid order', async () => {
    const payload = { paymentMethod: 'cash', price: 7.5, ingredients: { bun: 'plain', patty: 'chicken' } };
    const res = await request(app).post('/orders').send(payload);

    expect(res.statusCode).toBe(201);
    expect(res.body).toMatchObject({ success: true });
    expect(res.body.data).toHaveProperty('id', 2);
    expect(res.body.data).toHaveProperty('orderNumber', 1002);
    expect(res.body.data.ingredients).toEqual(payload.ingredients);
    createdId = res.body.data.id;
  });

  test('GET /orders/:id returns the created order', async () => {
    const postRes = await request(app).post('/orders').send({ paymentMethod: 'cash', price: 7.5, ingredients: { bun: 'plain', patty: 'chicken' } });
    createdId = postRes.body.data.id;

    const res = await request(app).get(`/orders/${createdId}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toMatchObject({ id: createdId, paymentMethod: 'cash' });
  });

  test('PUT /orders/:id should update existing order', async () => {
    const postRes = await request(app).post('/orders').send({ paymentMethod: 'cash', price: 7.5, ingredients: { bun: 'plain', patty: 'chicken' } });
    createdId = postRes.body.data.id;

    const res = await request(app).put(`/orders/${createdId}`).send({ paymentMethod: 'card', price: 8.0, ingredients: { bun: 'sesame', patty: 'beef' } });
    expect(res.statusCode).toBe(200);
    expect(res.body.data.paymentMethod).toBe('card');
    expect(res.body.data.price).toBe(8.0);
  });

  test('DELETE /orders/:id returns deleted order data', async () => {
    const postRes = await request(app).post('/orders').send({ paymentMethod: 'cash', price: 7.5, ingredients: { bun: 'plain', patty: 'chicken' } });
    createdId = postRes.body.data.id;

    const res = await request(app).delete(`/orders/${createdId}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.data.id).toBe(createdId);
    expect(res.body.success).toBe(true);
  });

  test('POST /orders returns 400 for invalid body', async () => {
    const res = await request(app).post('/orders').send({ price: -1, ingredients: {} });
    expect(res.statusCode).toBe(400);
    expect(res.body).toEqual(expect.objectContaining({ success: false, message: 'Validation failed' }));
    expect(res.body.errors).toEqual(expect.arrayContaining([expect.stringContaining('paymentMethod')]));
  });

  test('GET /orders/999 returns 404 when order not found', async () => {
    const res = await request(app).get('/orders/999');
    expect(res.statusCode).toBe(404);
    expect(res.body).toEqual(expect.objectContaining({ success: false, message: 'Order not found' }));
  });

  test('PUT /orders/abc returns 400 for invalid id', async () => {
    const res = await request(app).put('/orders/abc').send({ paymentMethod: 'cash', price: 5.0, ingredients: { bun: 'plain' } });
    expect(res.statusCode).toBe(400);
    expect(res.body).toEqual(expect.objectContaining({ success: false, message: 'Invalid order ID' }));
  });

  test('DELETE /orders/999 returns 404 when deleting missing order', async () => {
    const res = await request(app).delete('/orders/999');
    expect(res.statusCode).toBe(404);
    expect(res.body).toEqual(expect.objectContaining({ success: false, message: 'Order not found' }));
  });
});
