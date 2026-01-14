const mysql = require('mysql2/promise');

// Configuración de la base de datos desde variables de entorno
const dbConfig = {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT || 3306,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME
};

exports.handler = async (event) => {
    console.log('Event received:', JSON.stringify(event));
    
    let connection;
    
    try {
        // Parsear el body si viene como string
        const body = typeof event.body === 'string' ? JSON.parse(event.body) : event.body;
        
        // Validar datos requeridos
        if (!body.username || !body.password) {
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    status: 'KO',
                    message: 'Username and password are required'
                })
            };
        }
        
        // Validar longitud de username y password
        if (body.username.length < 3 || body.password.length < 6) {
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    status: 'KO',
                    message: 'Username must be at least 3 characters and password at least 6 characters'
                })
            };
        }
        
        // Conectar a la base de datos
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        const username = body.username;
        const password = body.password;
        const email = body.email || null;
        
        // Verificar si el usuario ya existe
        const checkQuery = 'SELECT user_id FROM users WHERE username = ?';
        const [existingUsers] = await connection.execute(checkQuery, [username]);
        
        if (existingUsers.length > 0) {
            console.log('Username already exists:', username);
            return {
                statusCode: 409,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    status: 'KO',
                    message: 'Username already exists'
                })
            };
        }
        
        // Insertar nuevo usuario
        const insertQuery = 'INSERT INTO users (username, password, email) VALUES (?, ?, ?)';
        const [result] = await connection.execute(insertQuery, [username, password, email]);
        
        console.log('User registered successfully:', username);
        
        // Respuesta exitosa
        return {
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            body: JSON.stringify({
                success: true,
                status: 'OK',
                message: 'User registered successfully',
                username: username,
                userId: result.insertId
            })
        };
        
    } catch (error) {
        console.error('Error:', error);
        
        return {
            statusCode: 500,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            body: JSON.stringify({
                success: false,
                status: 'KO',
                message: 'Error during registration',
                error: error.message
            })
        };
        
    } finally {
        // Cerrar conexión
        if (connection) {
            await connection.end();
            console.log('Database connection closed');
        }
    }
};
