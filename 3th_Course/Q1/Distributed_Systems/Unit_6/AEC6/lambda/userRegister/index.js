const mysql = require('mysql2/promise');

// He configurado la conexion a la base de datos usando variables de entorno
// esto me permite cambiar los parametros sin modificar el codigo
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
        // Primero parseo el body porque Lambda puede enviarlo como string o como objeto
        const body = typeof event.body === 'string' ? JSON.parse(event.body) : event.body;
        
        // Valido que los campos obligatorios esten presentes antes de continuar
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
        
        // Valido la longitud minima de usuario y contraseña por seguridad
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
        
        // Establezco la conexion con la base de datos RDS
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        const username = body.username;
        const password = body.password;
        const email = body.email || null;
        
        // Verifico si el usuario ya existe en la base de datos
        const checkQuery = 'SELECT user_id FROM users WHERE username = ?';
        const [existingUsers] = await connection.execute(checkQuery, [username]);
        
        if (existingUsers.length > 0) {
            console.log('Username already exists:', username);
            // Devuelvo KO porque el usuario ya existe
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
        
        // Inserto el nuevo usuario en la tabla users
        const insertQuery = 'INSERT INTO users (username, password, email) VALUES (?, ?, ?)';
        const [result] = await connection.execute(insertQuery, [username, password, email]);
        
        console.log('User registered successfully:', username);
        
        // Devuelvo OK para que el frontend redirija a login
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
        
        // En caso de error devuelvo un mensaje descriptivo
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
        // Siempre cierro la conexion a la base de datos para liberar recursos
        if (connection) {
            await connection.end();
            console.log('Database connection closed');
        }
    }
};
