--Ejercicio 1: Consulta vulnerable a SQL Injection
SELECT * FROM usuarios WHERE username = '' OR 1=1 --' AND password = 'cualquier valor';

--Ejercicio 2: Prevención con consultas parametrizadas
-- Consulta segura utilizando parámetros (en PHP como ejemplo)
$stmt = $pdo->prepare("SELECT * FROM usuarios WHERE username = :username AND password = :password");
$stmt->execute(['username' => $username, 'password' => $password]);

--Ejercicio 3: Consulta vulnerable a SQL Injection con UNION
-- Consulta vulnerable
SELECT name, email FROM usuarios WHERE id = '$id';
SELECT name, email FROM usuarios WHERE id = '' UNION SELECT username, password FROM admin --';

--Ejercicio 4: Prevención con consultas parametrizadas y UNION
-- Consulta segura utilizando parámetros (en PHP como ejemplo)
$stmt = $pdo->prepare("SELECT name, email FROM usuarios WHERE id = :id UNION SELECT username, password FROM admin");
$stmt->execute(['id' => $id]);

--Ejercicio 5: Prevención con validación de entradas
-- Validar que el parámetro es un número (en caso de que solo se permita números)
SELECT * FROM productos WHERE id = $id;

-- Asegurarse de que $id es un valor numérico y no contiene caracteres no permitidos.
if (!is_numeric($id)) {
    die("Input no válido");
}

--Ejercicio 6: Uso de procedimientos almacenados para prevenir SQL Injection
-- Procedimiento almacenado para realizar la consulta de forma segura
DELIMITER $$

CREATE PROCEDURE obtener_usuario(IN p_username VARCHAR(100), IN p_password VARCHAR(100))
BEGIN
    SELECT * FROM usuarios WHERE username = p_username AND password = p_password;
END $$

DELIMITER ;

$stmt = $pdo->prepare("CALL obtener_usuario(:username, :password)");
$stmt->execute(['username' => $username, 'password' => $password]);


--Ejercicio 7: Uso de ORM para prevenir SQL Injection
-- Uso de un ORM (como Eloquent en Laravel) para realizar consultas seguras
$usuario = Usuario::where('username', $username)->where('password', $password)->first();

--Ejercicio 8: Uso de funciones hash para almacenar contraseñas
-- Almacenar contraseñas de forma segura utilizando hash

$passwordHash = password_hash($password, PASSWORD_BCRYPT);
$stmt = $pdo->prepare("INSERT INTO usuarios (username, password) VALUES (:username, :password)");
$stmt->execute(['username' => $username, 'password' => $passwordHash]);
-- Verificar la contraseña al iniciar sesión
$stmt = $pdo->prepare("SELECT * FROM usuarios WHERE username = :username");
$stmt->execute(['username' => $username]);
$usuario = $stmt->fetch();
if (password_verify($password, $usuario['password'])) {
    // Contraseña correcta
} else {
    // Contraseña incorrecta
}

--Ejercicio 9: Uso de roles y permisos para limitar el acceso
-- Implementar un sistema de roles y permisos para limitar el acceso a ciertas consultas
-- Ejemplo de tabla de roles
CREATE TABLE roles (
    role_id INT PRIMARY KEY,
    role_name VARCHAR(50)
);
-- Ejemplo de tabla de permisos
CREATE TABLE permisos (
    permiso_id INT PRIMARY KEY,
    permiso_name VARCHAR(50)
);
-- Ejemplo de tabla de asignación de roles a usuarios
CREATE TABLE usuario_roles (
    usuario_id INT,
    role_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);
-- Ejemplo de tabla de asignación de permisos a roles
CREATE TABLE rol_permisos (
    role_id INT,
    permiso_id INT,
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (permiso_id) REFERENCES permisos(permiso_id)
);
-- Ejemplo de verificación de permisos antes de realizar una consulta
$usuario = Usuario::find($usuario_id);
$roles = $usuario->roles;
$permisos = [];
foreach ($roles as $role) {
    $permisos = array_merge($permisos, $role->permisos);
}
if (in_array('ver_usuarios', $permisos)) {
    // El usuario tiene permiso para ver usuarios
    $stmt = $pdo->prepare("SELECT * FROM usuarios");
    $stmt->execute();
    $usuarios = $stmt->fetchAll();
} else {
    // El usuario no tiene permiso
}
