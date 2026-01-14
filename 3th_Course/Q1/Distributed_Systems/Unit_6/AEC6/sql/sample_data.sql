-- ============================================
-- Mini Twitter - Sample Data
-- Datos de prueba para testing
-- ============================================

USE minitwitter;

-- ============================================
-- Insertar usuarios de prueba
-- Contraseñas: todas son "password123"
-- En producción deberían estar hasheadas
-- ============================================
INSERT INTO users (username, password, email) VALUES
('admin', 'password123', 'admin@minitwitter.com'),
('juan_perez', 'password123', 'juan@example.com'),
('maria_garcia', 'password123', 'maria@example.com'),
('test_user', 'password123', 'test@example.com');

-- ============================================
-- Insertar comentarios de prueba
-- ============================================
INSERT INTO comments (username, comment_text, video_url, video_filename) VALUES
('admin', '¡Bienvenidos a Mini Twitter! Este es el primer post del sistema.', 
 'https://your-bucket.s3.amazonaws.com/videos/welcome.mp4', 'welcome.mp4'),

('juan_perez', 'Probando la funcionalidad de posts. ¡Funciona genial!', 
 NULL, NULL),

('maria_garcia', 'Compartiendo un video interesante sobre AWS Lambda.', 
 'https://your-bucket.s3.amazonaws.com/videos/aws-tutorial.mp4', 'aws-tutorial.mp4'),

('admin', 'Recuerden revisar la documentación de AWS para configurar correctamente RDS.', 
 NULL, NULL),

('test_user', 'Este es un comentario de prueba con un video adjunto.', 
 'https://your-bucket.s3.amazonaws.com/videos/test-video.mp4', 'test-video.mp4');

-- ============================================
-- Verificar datos insertados
-- ============================================
SELECT '=== USUARIOS REGISTRADOS ===' AS info;
SELECT user_id, username, email, created_at FROM users;

SELECT '=== COMENTARIOS PUBLICADOS ===' AS info;
SELECT comment_id, username, 
       LEFT(comment_text, 50) AS comment_preview, 
       video_filename, 
       created_at 
FROM comments 
ORDER BY created_at DESC;

-- ============================================
-- Queries útiles para testing
-- ============================================

-- Contar comentarios por usuario
SELECT '=== COMENTARIOS POR USUARIO ===' AS info;
SELECT username, COUNT(*) as total_comments 
FROM comments 
GROUP BY username 
ORDER BY total_comments DESC;

-- Ver comentarios con videos
SELECT '=== COMENTARIOS CON VIDEO ===' AS info;
SELECT comment_id, username, video_filename 
FROM comments 
WHERE video_url IS NOT NULL;

-- Último comentario de cada usuario
SELECT '=== ÚLTIMO COMENTARIO POR USUARIO ===' AS info;
SELECT c1.username, c1.comment_text, c1.created_at
FROM comments c1
INNER JOIN (
    SELECT username, MAX(created_at) as max_date
    FROM comments
    GROUP BY username
) c2 ON c1.username = c2.username AND c1.created_at = c2.max_date;
