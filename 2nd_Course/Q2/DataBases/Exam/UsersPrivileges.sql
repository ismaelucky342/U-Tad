-- Ejercicios de gestión de usuarios y permisos en SQL

-- 1. Crear un usuario llamado 'usuario1' con contraseña 'password123'
CREATE USER 'usuario1'@'localhost' IDENTIFIED BY 'password123';

-- 2. Conceder permisos de solo lectura sobre la base de datos 'universidad'
GRANT SELECT ON universidad.* TO 'usuario1'@'localhost';

-- 3. Crear un usuario 'admin_db' con todos los privilegios sobre la base de datos 'universidad'
CREATE USER 'admin_db'@'localhost' IDENTIFIED BY 'adminpass';
GRANT ALL PRIVILEGES ON universidad.* TO 'admin_db'@'localhost';

-- 4. Revocar el permiso de borrado (DELETE) al usuario 'usuario1'
REVOKE DELETE ON universidad.* FROM 'usuario1'@'localhost';

-- 5. Cambiar la contraseña del usuario 'usuario1'
ALTER USER 'usuario1'@'localhost' IDENTIFIED BY 'nuevaPassword';

-- 6. Eliminar el usuario 'usuario1'
DROP USER 'usuario1'@'localhost';

-- 7. Ver los privilegios de un usuario
SHOW GRANTS FOR 'admin_db'@'localhost';

-- 8. Crear un usuario solo con acceso a una tabla específica
CREATE USER 'lector_tabla'@'localhost' IDENTIFIED BY 'lectura';
GRANT SELECT ON universidad.estudiantes TO 'lector_tabla'@'localhost';

-- 9. Revocar todos los privilegios de 'admin_db' sobre la base de datos 'universidad'
REVOKE ALL PRIVILEGES ON universidad.* FROM 'admin_db'@'localhost';

-- 10. Eliminar el usuario 'admin_db'
DROP USER 'admin_db'@'localhost';

-- 11. Ver todos los usuarios existentes
SELECT User, Host FROM mysql.user;

-- 12. Conceder permisos de inserción y actualización a 'lector_tabla' solo en la tabla 'estudiantes'
GRANT INSERT, UPDATE ON universidad.estudiantes TO 'lector_tabla'@'localhost';

-- 13. Revocar el permiso de actualización (UPDATE) a 'lector_tabla' en la tabla 'estudiantes'
REVOKE UPDATE ON universidad.estudiantes FROM 'lector_tabla'@'localhost';

-- 14. Cambiar el nombre de usuario de 'lector_tabla' a 'lector_estudiantes'
RENAME USER 'lector_tabla'@'localhost' TO 'lector_estudiantes'@'localhost';

-- 15. Eliminar el usuario 'lector_estudiantes'
DROP USER 'lector_estudiantes'@'localhost';

-- 16. Crear un usuario 'backup_user' con permisos de solo lectura en todas las tablas de la base de datos 'universidad'
CREATE USER 'backup_user'@'localhost' IDENTIFIED BY 'backupPass';
GRANT SELECT ON universidad.* TO 'backup
_user'@'localhost';

-- 17. Revocar el permiso de lectura (SELECT) a 'backup_user' en la base de datos 'universidad'
REVOKE SELECT ON universidad.* FROM 'backup_user'@'localhost';

-- 18. Eliminar el usuario 'backup_user'
DROP USER 'backup_user'@'localhost';

-- 19. Crear un usuario 'profesor' con permisos de inserción y selección en la tabla 'asignaturas'
CREATE USER 'profesor'@'localhost' IDENTIFIED BY 'profesorPass';
GRANT INSERT, SELECT ON universidad.asignaturas TO 'profesor'@'localhost';

-- 20. Revocar el permiso de inserción (INSERT) a 'profesor' en la tabla 'asignaturas'
REVOKE INSERT ON universidad.asignaturas FROM 'profesor'@'localhost';

-- 21. Cambiar la contraseña del usuario 'profesor'
ALTER USER 'profesor'@'localhost' IDENTIFIED BY 'nuevaProfPass';

-- 22. Eliminar el usuario 'profesor'
DROP USER 'profesor'@'localhost';

-- 23. Crear un usuario 'consultor' con permisos de solo lectura en la tabla 'profesores'
CREATE USER 'consultor'@'localhost' IDENTIFIED BY 'consultorPass';
GRANT SELECT ON universidad.profesores TO 'consultor'@'localhost';

-- 24. Revocar el permiso de lectura (SELECT) a 'consultor' en la tabla 'profesores'
REVOKE SELECT ON universidad.profesores FROM 'consultor'@'localhost';

-- 25. Eliminar el usuario 'consultor'
DROP USER 'consultor'@'localhost';