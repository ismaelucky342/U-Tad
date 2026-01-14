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
        // Obtener parámetros de query string
        const username = event.queryStringParameters?.username;
        
        if (!username) {
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'GET, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    message: 'Username parameter is required'
                })
            };
        }
        
        // Conectar a la base de datos
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        // Query para obtener comentarios de un usuario específico
        const query = `
            SELECT 
                comment_id,
                username,
                comment_text,
                video_url,
                video_filename,
                created_at,
                likes
            FROM comments 
            WHERE username = ?
            ORDER BY created_at DESC
        `;
        
        const [rows] = await connection.execute(query, [username]);
        
        console.log(`Retrieved ${rows.length} comments for user: ${username}`);
        
        // Respuesta exitosa
        return {
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, OPTIONS'
            },
            body: JSON.stringify({
                success: true,
                message: `Comments retrieved successfully for user: ${username}`,
                username: username,
                count: rows.length,
                comments: rows
            })
        };
        
    } catch (error) {
        console.error('Error:', error);
        
        return {
            statusCode: 500,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, OPTIONS'
            },
            body: JSON.stringify({
                success: false,
                message: 'Error retrieving comments',
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
