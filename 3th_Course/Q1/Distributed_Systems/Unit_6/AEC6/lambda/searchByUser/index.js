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
        // Obtengo el parametro username desde la query string de la peticion GET
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
        
        // Establezco la conexion con la base de datos RDS
        connection = await mysql.createConnection(dbConfig);
        console.log('Database connection established');
        
        // Obtengo solo los comentarios del usuario especificado ordenados por fecha
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
        
        // Devuelvo los comentarios filtrados por usuario
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
        
        // En caso de error devuelvo un mensaje descriptivo
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
        // Siempre cierro la conexion a la base de datos para liberar recursos
        if (connection) {
            await connection.end();
            console.log('Database connection closed');
        }
    }
};
