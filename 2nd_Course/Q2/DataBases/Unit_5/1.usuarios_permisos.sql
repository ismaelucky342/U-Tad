-- Crear un usuario con permisos limitados
CREATE USER 'usuario_test'@'localhost' IDENTIFIED BY 'password123';

-- Otorgar permisos específicos sobre una base de datos
GRANT SELECT, INSERT, UPDATE ON test_db.* TO 'usuario_test'@'localhost';

-- Verificar los permisos del usuario
SHOW GRANTS FOR 'usuario_test'@'localhost';

-- Revocar permisos
REVOKE INSERT ON test_db.* FROM 'usuario_test'@'localhost';

-- Eliminar el usuario
DROP USER 'usuario_test'@'localhost';
