const request = require('supertest');
const app = require('../src/index');
const User = require('../src/models/User');
const mongoose = require('mongoose');

describe('Auth API', () => {
  beforeAll(async () => {
    process.env.NODE_ENV = 'test';
    await mongoose.connect(process.env.MONGODB_URI_TEST, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });
    await User.deleteMany({});
  });

  afterAll(async () => {
    await User.deleteMany({});
    await mongoose.connection.close();
  });

  // Tests para registro del primer usuario
  test('POST /auth/register - Registrar primer usuario exitosamente', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Admin User',
        username: 'admin',
        email: 'admin@example.com',
        phone: '+34666666666',
        position: 'Admin',
        password: 'password123'
      });

    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body).toHaveProperty('token');
    expect(res.body.user.email).toBe('admin@example.com');
  });

  test('POST /auth/register - Falla al registrar segundo usuario sin autenticación', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Second User',
        username: 'user2',
        email: 'user2@example.com',
        phone: '+34666666667',
        position: 'Staff',
        password: 'password123'
      });

    expect(res.statusCode).toBe(403);
    expect(res.body.success).toBe(false);
  });

  test('POST /auth/register - Falla con datos duplicados', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Duplicate User',
        username: 'admin',
        email: 'admin@example.com',
        phone: '+34666666668',
        position: 'Staff',
        password: 'password123'
      });

    expect(res.statusCode).toBe(400);
    expect(res.body.success).toBe(false);
  });

  test('POST /auth/register - Falla con validaciones incompletas', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Test',
        username: 'test',
        email: 'invalid-email',
        phone: '+34666666669',
        position: 'Staff'
      });

    expect(res.statusCode).toBe(400);
  });

  // Tests para login
  test('POST /auth/login - Login exitoso', async () => {
    const res = await request(app)
      .post('/auth/login')
      .send({
        email: 'admin@example.com',
        password: 'password123'
      });

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body).toHaveProperty('token');
    expect(res.body.user.email).toBe('admin@example.com');
  });

  test('POST /auth/login - Falla con email incorrecto', async () => {
    const res = await request(app)
      .post('/auth/login')
      .send({
        email: 'nonexistent@example.com',
        password: 'password123'
      });

    expect(res.statusCode).toBe(401);
    expect(res.body.success).toBe(false);
  });

  test('POST /auth/login - Falla con contraseña incorrecta', async () => {
    const res = await request(app)
      .post('/auth/login')
      .send({
        email: 'admin@example.com',
        password: 'wrongpassword'
      });

    expect(res.statusCode).toBe(401);
    expect(res.body.success).toBe(false);
  });

  test('POST /auth/login - Falla sin email y contraseña', async () => {
    const res = await request(app)
      .post('/auth/login')
      .send({});

    expect(res.statusCode).toBe(400);
  });

  // Tests para obtener usuario actual
  test('GET /auth/me - Obtener usuario actual con token válido', async () => {
    const loginRes = await request(app)
      .post('/auth/login')
      .send({
        email: 'admin@example.com',
        password: 'password123'
      });

    const res = await request(app)
      .get('/auth/me')
      .set('Authorization', `Bearer ${loginRes.body.token}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.user.email).toBe('admin@example.com');
  });

  test('GET /auth/me - Falla sin token', async () => {
    const res = await request(app)
      .get('/auth/me');

    expect(res.statusCode).toBe(401);
    expect(res.body.success).toBe(false);
  });

  test('GET /auth/me - Falla con token inválido', async () => {
    const res = await request(app)
      .get('/auth/me')
      .set('Authorization', 'Bearer invalid_token');

    expect(res.statusCode).toBe(401);
    expect(res.body.success).toBe(false);
  });

  // Tests para logout
  test('POST /auth/logout - Logout exitoso', async () => {
    const loginRes = await request(app)
      .post('/auth/login')
      .send({
        email: 'admin@example.com',
        password: 'password123'
      });

    const res = await request(app)
      .post('/auth/logout')
      .set('Authorization', `Bearer ${loginRes.body.token}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
  });

  test('POST /auth/logout - Falla sin autenticación', async () => {
    const res = await request(app)
      .post('/auth/logout');

    expect(res.statusCode).toBe(401);
  });
});
