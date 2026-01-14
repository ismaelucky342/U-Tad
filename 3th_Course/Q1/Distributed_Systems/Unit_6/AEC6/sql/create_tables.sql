-- ============================================
-- Mini Twitter - Database Schema
-- Sistema de comentarios y usuarios
-- ============================================

-- Crear base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS minitwitter;
USE minitwitter;

-- ============================================
-- Tabla: users
-- Almacena información de usuarios registrados
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- Tabla: comments
-- Almacena los comentarios/posts de usuarios
-- ============================================
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

-- ============================================
-- Verificar tablas creadas
-- ============================================
SHOW TABLES;

-- Ver estructura de la tabla users
DESCRIBE users;

-- Ver estructura de la tabla comments
DESCRIBE comments;

-- ============================================
-- Información adicional
-- ============================================
SELECT 'Base de datos creada exitosamente' AS status;
SELECT COUNT(*) AS total_users FROM users;
SELECT COUNT(*) AS total_comments FROM comments;
