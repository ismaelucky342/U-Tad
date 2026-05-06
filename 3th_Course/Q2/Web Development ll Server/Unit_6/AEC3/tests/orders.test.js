const request = require('supertest');
const app = require('../src/index');
const Order = require('../src/models/Order');
const Product = require('../src/models/Product');
const User = require('../src/models/User');
const mongoose = require('mongoose');

// Variables globales para tests
let authToken;
let userId;
let productId;
let orderId;

describe('Orders API', () => {
  beforeAll(async () => {
    // Conectar a BD de prueba
    process.env.NODE_ENV = 'test';
    await mongoose.connect(process.env.MONGODB_URI_TEST, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });

    // Limpiar colecciones
    await Order.deleteMany({});
    await Product.deleteMany({});
    await User.deleteMany({});

    // Crear usuario de prueba
    const userRes = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Test User',
        username: 'testuser',
        email: 'test@example.com',
        phone: '+34666666666',
        position: 'Admin',
        password: 'password123'
      });
    
    authToken = userRes.body.token;
    userId = userRes.body.user.id;

    // Crear producto de prueba
    const productRes = await request(app)
      .post('/products')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Hamburguesa Clásica',
        description: 'Deliciosa hamburguesa con queso y lechuga',
        price: 9.99,
        ingredients: 'Pan, carne, queso, lechuga, tomate'
      });
    
    productId = productRes.body.product._id;
  });

  afterAll(async () => {
    await Order.deleteMany({});
    await Product.deleteMany({});
    await User.deleteMany({});
    await mongoose.connection.close();
  });

  // Tests para crear órdenes
  test('POST /orders - Crear una orden válida', async () => {
    const res = await request(app)
      .post('/orders')
      .send({
        paymentMethod: 'Cash',
        deliveryAddress: '123 Main St',
        products: [
          {
            productId: productId,
            quantity: 2
          }
        ],
        customer: {
          name: 'John Doe',
          email: 'john@example.com',
          phone: '+34666666666'
        }
      });

    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body.order).toHaveProperty('orderNumber');
    expect(res.body.order.totalPrice).toBe(19.98); // 9.99 * 2
    orderId = res.body.order._id;
  });

  test('POST /orders - Falla sin productos', async () => {
    const res = await request(app)
      .post('/orders')
      .send({
        paymentMethod: 'Cash',
        deliveryAddress: '123 Main St',
        products: [],
        customer: { name: 'John Doe' }
      });

    expect(res.statusCode).toBe(400);
    expect(res.body.success).toBe(false);
  });

  test('POST /orders - Falla con método de pago inválido', async () => {
    const res = await request(app)
      .post('/orders')
      .send({
        paymentMethod: 'InvalidMethod',
        products: [{ productId: productId, quantity: 1 }],
        customer: { name: 'John Doe' }
      });

    expect(res.statusCode).toBe(400);
  });

  // Tests para obtener órdenes
  test('GET /orders - Obtener todas las órdenes (requiere autenticación)', async () => {
    const res = await request(app)
      .get('/orders')
      .set('Authorization', `Bearer ${authToken}`);

    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body.orders)).toBe(true);
  });

  test('GET /orders - Falla sin autenticación', async () => {
    const res = await request(app)
      .get('/orders');

    expect(res.statusCode).toBe(401);
  });

  test('GET /orders/:id - Obtener orden específica', async () => {
    const res = await request(app)
      .get(`/orders/${orderId}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.order._id).toBe(orderId.toString());
  });

  test('GET /orders/:id - Falla con ID inválido', async () => {
    const res = await request(app)
      .get('/orders/invalidid');

    expect(res.statusCode).toBe(500);
  });

  // Tests para actualizar estado de órdenes
  test('PUT /orders/:id/status - Actualizar estado de orden', async () => {
    const res = await request(app)
      .put(`/orders/${orderId}/status`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        status: 'Confirmed'
      });

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.order.status).toBe('Confirmed');
  });

  test('PUT /orders/:id/status - Falla sin autenticación', async () => {
    const res = await request(app)
      .put(`/orders/${orderId}/status`)
      .send({ status: 'Confirmed' });

    expect(res.statusCode).toBe(401);
  });

  test('PUT /orders/:id/status - Falla con estado inválido', async () => {
    const res = await request(app)
      .put(`/orders/${orderId}/status`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({ status: 'InvalidStatus' });

    expect(res.statusCode).toBe(400);
  });

  // Tests para eliminar órdenes
  test('DELETE /orders/:id - Eliminar orden', async () => {
    const res = await request(app)
      .delete(`/orders/${orderId}`)
      .set('Authorization', `Bearer ${authToken}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
  });

  test('DELETE /orders/:id - Falla sin autenticación', async () => {
    const res = await request(app)
      .delete(`/orders/${orderId}`);

    expect(res.statusCode).toBe(401);
  });
});
