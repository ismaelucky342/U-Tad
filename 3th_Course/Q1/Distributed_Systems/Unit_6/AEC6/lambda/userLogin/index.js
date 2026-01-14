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
        
        // Conectar a la base de datos
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        const username = body.username;
        const password = body.password;
        
        // Buscar usuario en la base de datos
        const query = 'SELECT user_id, username, password FROM users WHERE username = ?';
        const [rows] = await connection.execute(query, [username]);
        
        // Verificar si el usuario existe y la contraseña es correcta
        if (rows.length === 0) {
            console.log('User not found:', username);
            return {
                statusCode: 401,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    status: 'KO',
                    message: 'Invalid username or password'
                })
            };
        }
        
        const user = rows[0];
        
        // Comparar contraseñas (en este caso simple, en producción usar bcrypt)
        if (user.password !== password) {
            console.log('Invalid password for user:', username);
            return {
                statusCode: 401,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    status: 'KO',
                    message: 'Invalid username or password'
                })
            };
        }
        
        // Actualizar último login
        const updateQuery = 'UPDATE users SET last_login = NOW() WHERE user_id = ?';
        await connection.execute(updateQuery, [user.user_id]);
        
        console.log('Login successful for user:', username);
        
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
                message: 'Login successful',
                username: username,
                userId: user.user_id
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
                message: 'Error during login',
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
