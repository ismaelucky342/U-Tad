const request = require('supertest');
const app = require('../src/index');
const User = require('../src/models/User');
const mongoose = require('mongoose');

describe('Users API', () => {
  let authToken;
  let adminId;
  let userId;

  beforeAll(async () => {
    process.env.NODE_ENV = 'test';
    await mongoose.connect(process.env.MONGODB_URI_TEST, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });

    await User.deleteMany({});

    // Crear usuario admin
    const adminRes = await request(app)
      .post('/auth/register')
      .send({
        fullName: 'Admin User',
        username: 'admin',
        email: 'admin@example.com',
        phone: '+34666666666',
        position: 'Admin',
        password: 'password123'
      });

    authToken = adminRes.body.token;
    adminId = adminRes.body.user.id;
  });

  afterAll(async () => {
    await User.deleteMany({});
    await mongoose.connection.close();
  });

  // Tests para crear usuarios
  test('POST /users - Crear usuario como admin exitosamente', async () => {
    const res = await request(app)
      .post('/users')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        fullName: 'Chef User',
        username: 'chef',
        email: 'chef@example.com',
        phone: '+34666666667',
        position: 'Chef',
        password: 'password123'
      });

    expect(res.statusCode).toBe(201);
    expect(res.body.success).toBe(true);
    expect(res.body.user.position).toBe('Chef');
    userId = res.body.user.id;
  });

  test('POST /users - Falla sin autenticación', async () => {
    const res = await request(app)
      .post('/users')
      .send({
        fullName: 'Test User',
        username: 'testuser',
        email: 'test@example.com',
        phone: '+34666666668',
        position: 'Staff',
        password: 'password123'
      });

    expect(res.statusCode).toBe(401);
  });

  test('POST /users - Falla si no es admin', async () => {
    // Primero crear un usuario no admin
    const nonAdminRes = await request(app)
      .post('/users')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        fullName: 'Staff User',
        username: 'staff',
        email: 'staff@example.com',
        phone: '+34666666669',
        position: 'Staff',
        password: 'password123'
      });

    const staffToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'staff@example.com',
        password: 'password123'
      })).body.token;

    const res = await request(app)
      .post('/users')
      .set('Authorization', `Bearer ${staffToken}`)
      .send({
        fullName: 'Another User',
        username: 'another',
        email: 'another@example.com',
        phone: '+34666666670',
        position: 'Staff',
        password: 'password123'
      });

    expect(res.statusCode).toBe(403);
  });

  test('POST /users - Falla con usuario duplicado', async () => {
    const res = await request(app)
      .post('/users')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        fullName: 'Duplicate User',
        username: 'chef',
        email: 'chef@example.com',
        phone: '+34666666671',
        position: 'Chef',
        password: 'password123'
      });

    expect(res.statusCode).toBe(400);
  });

  // Tests para obtener usuarios
  test('GET /users - Obtener todos los usuarios como admin', async () => {
    const res = await request(app)
      .get('/users')
      .set('Authorization', `Bearer ${authToken}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(Array.isArray(res.body.users)).toBe(true);
    expect(res.body.count).toBeGreaterThanOrEqual(1);
  });

  test('GET /users - Falla sin autenticación', async () => {
    const res = await request(app)
      .get('/users');

    expect(res.statusCode).toBe(401);
  });

  test('GET /users - Falla si no es admin', async () => {
    const staffToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'staff@example.com',
        password: 'password123'
      })).body.token;

    const res = await request(app)
      .get('/users')
      .set('Authorization', `Bearer ${staffToken}`);

    expect(res.statusCode).toBe(403);
  });

  test('GET /users/:id - Obtener usuario específico', async () => {
    const res = await request(app)
      .get(`/users/${userId}`)
      .set('Authorization', `Bearer ${authToken}`);

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.user._id).toBe(userId.toString());
  });

  test('GET /users/:id - Falla con ID inválido', async () => {
    const res = await request(app)
      .get('/users/invalidid')
      .set('Authorization', `Bearer ${authToken}`);

    expect(res.statusCode).toBe(500);
  });

  // Tests para actualizar usuarios
  test('PUT /users/:id - Actualizar usuario exitosamente', async () => {
    const res = await request(app)
      .put(`/users/${userId}`)
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        fullName: 'Chef Updated',
        phone: '+34700000000'
      });

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
    expect(res.body.user.fullName).toBe('Chef Updated');
  });

  test('PUT /users/:id - Usuario puede actualizar su propio perfil', async () => {
    const chefToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'chef@example.com',
        password: 'password123'
      })).body.token;

    const res = await request(app)
      .put(`/users/${userId}`)
      .set('Authorization', `Bearer ${chefToken}`)
      .send({
        phone: '+34711111111'
      });

    expect(res.statusCode).toBe(200);
    expect(res.body.user.phone).toBe('+34711111111');
  });

  test('PUT /users/:id - Usuario no puede actualizar otro perfil sin ser admin', async () => {
    const staffToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'staff@example.com',
        password: 'password123'
      })).body.token;

    const res = await request(app)
      .put(`/users/${userId}`)
      .set('Authorization', `Bearer ${staffToken}`)
      .send({
        phone: '+34722222222'
      });

    expect(res.statusCode).toBe(403);
  });

  // Tests para cambiar contraseña
  test('PUT /users/:id/change-password - Cambiar contraseña exitosamente', async () => {
    const chefToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'chef@example.com',
        password: 'password123'
      })).body.token;

    const res = await request(app)
      .put(`/users/${userId}/change-password`)
      .set('Authorization', `Bearer ${chefToken}`)
      .send({
        currentPassword: 'password123',
        newPassword: 'newpassword123'
      });

    expect(res.statusCode).toBe(200);
    expect(res.body.success).toBe(true);
  });

  test('PUT /users/:id/change-password - Falla con contraseña actual incorrecta', async () => {
    const chefToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'chef@example.com',
        password: 'newpassword123'
      })).body.token;

    const res = await request(app)
      .put(`/users/${userId}/change-password`)
      .set('Authorization', `Bearer ${chefToken}`)
      .send({
        currentPassword: 'wrongpassword',
        newPassword: 'anotherpassword'
      });

    expect(res.statusCode).toBe(401);
  });

  // Tests para eliminar usuarios
  test('DELETE /users/:id - Eliminar usuario como admin', async () => {
    // Crear un usuario temporal para eliminar
    const tempRes = await request(app)
      .post('/users')
      .set('Authorization', `Bearer ${authToken}`)
      .send({
        fullName: 'Temp User',
        username: 'tempuser',
        email: 'temp@example.com',
        phone: '+34666666672',
        position: 'Staff',
        password: 'password123'
      });

    const deleteRes = await request(app)
      .delete(`/users/${tempRes.body.user.id}`)
      .set('Authorization', `Bearer ${authToken}`);

    expect(deleteRes.statusCode).toBe(200);
    expect(deleteRes.body.success).toBe(true);
  });

  test('DELETE /users/:id - Falla sin autenticación', async () => {
    const res = await request(app)
      .delete(`/users/${userId}`);

    expect(res.statusCode).toBe(401);
  });

  test('DELETE /users/:id - Falla si no es admin', async () => {
    const staffToken = (await request(app)
      .post('/auth/login')
      .send({
        email: 'staff@example.com',
        password: 'password123'
      })).body.token;

    const res = await request(app)
      .delete(`/users/${userId}`)
      .set('Authorization', `Bearer ${staffToken}`);

    expect(res.statusCode).toBe(403);
  });
});
