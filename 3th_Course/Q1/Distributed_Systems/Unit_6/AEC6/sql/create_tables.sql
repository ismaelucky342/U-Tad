-- He diseñado el esquema de la base de datos para soportar un sistema tipo mini-Twitter
-- Incluye tablas para usuarios y comentarios con sus relaciones

-- Creo la base de datos si no existe previamente
CREATE DATABASE IF NOT EXISTS minitwitter;
USE minitwitter;

-- Tabla users: almaceno la informacion de los usuarios registrados
-- Incluyo username unico, password, email opcional y timestamps de creacion y ultimo acceso
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla comments: almaceno los comentarios/posts que publican los usuarios
-- Cada comentario puede tener opcionalmente un video adjunto almacenado en S3
CREATE TABLE IF NOT EXISTS comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    comment_text TEXT NOT NULL,
    video_url VARCHAR(500),
    video_filename VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    likes INT DEFAULT 0,
    INDEX idx_username (username),
    INDEX idx_created_at (created_at DESC),
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Verifico que las tablas se hayan creado correctamente
SHOW TABLES;

-- Muestro la estructura de la tabla users
DESCRIBE users;

-- Muestro la estructura de la tabla comments
DESCRIBE comments;

-- Informacion adicional para verificar el estado inicial
SELECT 'Base de datos creada exitosamente' AS status;
SELECT COUNT(*) AS total_users FROM users;
SELECT COUNT(*) AS total_comments FROM comments;
