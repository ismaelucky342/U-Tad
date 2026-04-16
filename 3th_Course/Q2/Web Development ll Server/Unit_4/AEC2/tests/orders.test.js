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

describe('Orders API', () => {
  let createdId;

  test('GET /orders should return array', async () => {
    const res = await request(app).get('/orders');
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('success', true);
    expect(Array.isArray(res.body.data)).toBe(true);
  });

  test('POST /orders should create an order', async () => {
    const payload = { paymentMethod: 'cash', price: 7.5, ingredients: { bun: 'plain', patty: 'chicken' } };
    const res = await request(app).post('/orders').send(payload);
    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body.data).toHaveProperty('id');
    createdId = res.body.data.id;
  });

  test('GET /orders/:id should return created order', async () => {
    const res = await request(app).get(`/orders/${createdId}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.data.id).toBe(createdId);
  });

  test('PUT /orders/:id should update order', async () => {
    const res = await request(app).put(`/orders/${createdId}`).send({ paymentMethod: 'card', price: 8.0, ingredients: { bun: 'sesame' } });
    expect(res.statusCode).toBe(200);
    expect(res.body.data.paymentMethod).toBe('card');
  });

  test('DELETE /orders/:id should remove order', async () => {
    const res = await request(app).delete(`/orders/${createdId}`);
    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
  });
});
