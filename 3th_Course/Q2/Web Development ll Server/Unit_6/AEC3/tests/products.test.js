const request = require('supertest');
const app = require('../src/index');
const Product = require('../src/models/Product');
const User = require('../src/models/User');
const mongoose = require('mongoose');

describe('Products API', () => {
  let authToken;
  let productId;
  let userId;

  beforeAll(async () => {
    process.env.NODE_ENV = 'test';
    await mongoose.connect(process.env.MONGODB_URI_TEST, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });

    await Product.deleteMany({});
    await User.deleteMany({});

    // Crear usuario de prueba
    const userRes = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Product Admin',
        username: 'productadmin',
        email: 'productadmin@example.com',
        phone: '+34666666666',
        position: 'Admin',
        password: 'password123'
      });

    authToken = userRes.body.token;
    userId = userRes.body.user.id;
  });

  afterAll(async () => {
    await Product.deleteMany({});
    await User.deleteMany({});
    await mongoose.connection.close();
  });

  // Tests para crear productos
  test('POST /products - Crear producto exitosamente', async () => {
    const res = await request(app)
      .post('/products')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Hamburguesa Premium',
        description: 'Deliciosa hamburguesa con carnes de alta calidad',
        price: 15.99,
        ingredients: 'Pan integral, carne premium, queso suizo, lechuga, tomate'
      });

    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body.product.name).toBe('Hamburguesa Premium');
    expect(res.body.product.price).toBe(15.99);
    productId = res.body.product._id;
  });

  test('POST /products - Falla sin autenticación', async () => {
    const res = await request(app)
      .post('/products')
      .send({
        name: 'Test Burger',
        description: 'Test description with at least ten characters',
        price: 9.99,
        ingredients: 'Test ingredients'
      });

    expect(res.statusCode).toBe(401);
  });

  test('POST /products - Falla con validaciones incompletas', async () => {
    const res = await request(app)
      .post('/products')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Test',
        description: 'Short',
        price: 'invalid',
        ingredients: 'Ingredients'
      });

    expect(res.statusCode).toBe(400);
  });

  test('POST /products - Falla con precio negativo', async () => {
    const res = await request(app)
      .post('/products')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Invalid Price Product',
        description: 'This has a valid description length',
        price: -5.99,
        ingredients: 'Some ingredients'
      });

    expect(res.statusCode).toBe(400);
  });

  test('POST /products - Falla con producto duplicado', async () => {
    const res = await request(app)
      .post('/products')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Hamburguesa Premium',
        description: 'Deliciosa hamburguesa con carnes de alta calidad',
        price: 15.99,
        ingredients: 'Pan integral, carne premium, queso suizo, lechuga, tomate'
      });

    expect(res.statusCode).toBe(400);
    expect(res.body.success).toBe(false);
  });

  // Tests para obtener productos
  test('GET /products - Obtener todos los productos', async () => {
    const res = await request(app)
      .get('/products');

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.products)).toBe(true);
    expect(res.body.count).toBeGreaterThanOrEqual(1);
  });

  test('GET /products - Filtrar por disponibilidad', async () => {
    const res = await request(app)
      .get('/products?available=true');

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.products)).toBe(true);
  });

  test('GET /products/:id - Obtener producto específico', async () => {
    const res = await request(app)
      .get(`/products/${productId}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.product._id).toBe(productId.toString());
  });

  test('GET /products/:id - Falla con ID inválido', async () => {
    const res = await request(app)
      .get('/products/invalidid');

    expect(res.statusCode).toBe(400);
  });

  test('GET /products/:id - Falla con producto no existente', async () => {
    const fakeId = new mongoose.Types.ObjectId();
    const res = await request(app)
      .get(`/products/${fakeId}`);

    expect(res.statusCode).toBe(404);
    expect(res.body.success).toBe(false);
  });

  // Tests para actualizar productos
  test('PUT /products/:id - Actualizar producto exitosamente', async () => {
    const res = await request(app)
      .put(`/products/${productId}`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Hamburguesa Premium Deluxe',
        price: 17.99,
        available: true
      });

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.product.name).toBe('Hamburguesa Premium Deluxe');
    expect(res.body.product.price).toBe(17.99);
  });

  test('PUT /products/:id - Falla sin autenticación', async () => {
    const res = await request(app)
      .put(`/products/${productId}`)
      .send({
        price: 20.00
      });

    expect(res.statusCode).toBe(401);
  });

  test('PUT /products/:id - Falla con producto no existente', async () => {
    const fakeId = new mongoose.Types.ObjectId();
    const res = await request(app)
      .put(`/products/${fakeId}`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        price: 20.00
      });

    expect(res.statusCode).toBe(404);
  });

  // Tests para eliminar productos
  test('DELETE /products/:id - Eliminar producto exitosamente', async () => {
    // Crear un nuevo producto para eliminar
    const createRes = await request(app)
      .post('/products')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        name: 'Producto para eliminar',
        description: 'Este es un producto que se va a eliminar',
        price: 5.99,
        ingredients: 'Ingredientes for testing'
      });

    const deleteRes = await request(app)
      .delete(`/products/${createRes.body.product._id}`)
      .set('Authorization', `Bearer ${authToken}`);

    expect(deleteRes.statusCode).toBe(200);
    expect(deleteRes.body.success).toBe(true);
  });

  test('DELETE /products/:id - Falla sin autenticación', async () => {
    const res = await request(app)
      .delete(`/products/${productId}`);

    expect(res.statusCode).toBe(401);
  });

  test('DELETE /products/:id - Falla con producto no existente', async () => {
    const fakeId = new mongoose.Types.ObjectId();
    const res = await request(app)
      .delete(`/products/${fakeId}`)
      .set('Authorization', `Bearer ${authToken}`);

    expect(res.statusCode).toBe(404);
  });
});
