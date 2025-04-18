-- Verificar si el servidor soporta conexiones SSL
SHOW VARIABLES LIKE 'have_ssl';

-- Crear usuario con conexión SSL
CREATE USER 'secure_user'@'localhost' 
IDENTIFIED BY 'secure_password'
REQUIRE SSL;

-- Otorgar permisos a este usuario
GRANT ALL PRIVILEGES ON test_db.* TO 'secure_user'@'localhost';

-- Verificación de conexiones SSL activas
SHOW STATUS LIKE 'Ssl_cipher';
