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
        if (!body.username || !body.comment_text) {
            return {
                statusCode: 400,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS'
                },
                body: JSON.stringify({
                    success: false,
                    message: 'Username and comment_text are required'
                })
            };
        }
        
        // Conectar a la base de datos
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        // Preparar datos del comentario
        const username = body.username;
        const commentText = body.comment_text;
        const videoUrl = body.video_url || null;
        const videoFilename = body.video_filename || null;
        
        // Insertar comentario en la base de datos
        const query = `
            INSERT INTO comments (username, comment_text, video_url, video_filename) 
            VALUES (?, ?, ?, ?)
        `;
        
        const [result] = await connection.execute(query, [
            username,
            commentText,
            videoUrl,
            videoFilename
        ]);
        
        console.log('Comment inserted successfully:', result.insertId);
        
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
                message: 'Comment posted successfully',
                commentId: result.insertId,
                data: {
                    username: username,
                    comment_text: commentText,
                    video_url: videoUrl,
                    video_filename: videoFilename
                }
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
                message: 'Error posting comment',
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
