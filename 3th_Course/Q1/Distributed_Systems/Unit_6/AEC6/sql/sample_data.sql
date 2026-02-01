-- He creado datos de prueba para poder testear todas las funcionalidades del sistema
-- Incluyo usuarios y comentarios de ejemplo para facilitar las pruebas

USE minitwitter;

-- Inserto usuarios de prueba con contraseñas simples
-- Nota: en produccion usaria bcrypt para hashear las contraseñas
INSERT INTO users (username, password, email) VALUES
('admin', 'password123', 'admin@minitwitter.com'),
('juan_perez', 'password123', 'juan@example.com'),
('maria_garcia', 'password123', 'maria@example.com'),
('test_user', 'password123', 'test@example.com');

-- Inserto comentarios de prueba, algunos con videos y otros sin ellos
INSERT INTO comments (username, comment_text, video_url, video_filename) VALUES
('admin', 'Bienvenidos a Mini Twitter! Este es el primer post del sistema.', 
 'https://your-bucket.s3.amazonaws.com/videos/welcome.mp4', 'welcome.mp4'),

('juan_perez', 'Probando la funcionalidad de posts. Funciona genial!', 
 NULL, NULL),

('maria_garcia', 'Compartiendo un video interesante sobre AWS Lambda.', 
 'https://your-bucket.s3.amazonaws.com/videos/aws-tutorial.mp4', 'aws-tutorial.mp4'),

('admin', 'Recuerden revisar la documentacion de AWS para configurar correctamente RDS.', 
 NULL, NULL),

('test_user', 'Este es un comentario de prueba con un video adjunto.', 
 'https://your-bucket.s3.amazonaws.com/videos/test-video.mp4', 'test-video.mp4');

-- Verifico que los datos se hayan insertado correctamente
SELECT '=== USUARIOS REGISTRADOS ===' AS info;
SELECT user_id, username, email, created_at FROM users;

SELECT '=== COMENTARIOS PUBLICADOS ===' AS info;
SELECT comment_id, username, 
       LEFT(comment_text, 50) AS comment_preview, 
       video_filename, 
       created_at 
FROM comments 
ORDER BY created_at DESC;

-- Queries utiles para verificar el funcionamiento del sistema durante las pruebas

-- Cuento comentarios por usuario
SELECT '=== COMENTARIOS POR USUARIO ===' AS info;
SELECT username, COUNT(*) as total_comments 
FROM comments 
GROUP BY username 
ORDER BY total_comments DESC;

-- Muestro solo los comentarios que tienen videos adjuntos
SELECT '=== COMENTARIOS CON VIDEO ===' AS info;
SELECT comment_id, username, video_filename 
FROM comments 
WHERE video_url IS NOT NULL;

-- Obtengo el ultimo comentario de cada usuario
SELECT '=== ULTIMO COMENTARIO POR USUARIO ===' AS info;
SELECT c1.username, c1.comment_text, c1.created_at
FROM comments c1
INNER JOIN (
    SELECT username, MAX(created_at) as max_date
    FROM comments
    GROUP BY username
) c2 ON c1.username = c2.username AND c1.created_at = c2.max_date;
