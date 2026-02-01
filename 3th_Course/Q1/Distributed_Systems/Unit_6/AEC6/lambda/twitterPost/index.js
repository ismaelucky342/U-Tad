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
        
        // Establezco la conexion con la base de datos RDS
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        // Extraigo los datos del comentario del body recibido
        const username = body.username;
        const commentText = body.comment_text;
        const videoUrl = body.video_url || null;
        const videoFilename = body.video_filename || null;
        
        // Inserto el comentario en la tabla comments usando prepared statements para evitar SQL injection
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
        
        // Devuelvo una respuesta exitosa con los datos del comentario creado
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
                message: 'Error posting comment',
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
