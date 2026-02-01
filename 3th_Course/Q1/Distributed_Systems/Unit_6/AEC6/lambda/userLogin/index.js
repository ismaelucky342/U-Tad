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
        
        // Establezco la conexion con la base de datos RDS
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        const username = body.username;
        const password = body.password;
        
        // Busco el usuario en la tabla users por su nombre de usuario
        const query = 'SELECT user_id, username, password FROM users WHERE username = ?';
        const [rows] = await connection.execute(query, [username]);
        
        // Verifico si el usuario existe en la base de datos
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
        
        // Comparo la contraseña proporcionada con la almacenada
        // Nota: en produccion usaria bcrypt para hashear las contraseñas
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
        
        // Actualizo la fecha del ultimo login del usuario
        const updateQuery = 'UPDATE users SET last_login = NOW() WHERE user_id = ?';
        await connection.execute(updateQuery, [user.user_id]);
        
        console.log('Login successful for user:', username);
        
        // Devuelvo OK para que el frontend redirija a postComment
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
                message: 'Error during login',
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
