-- Crear la tabla de clientes
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    fecha_registro DATE
);

-- Crear el procedimiento almacenado para insertar un cliente
DELIMITER $$

CREATE PROCEDURE insertar_cliente (
    IN p_cliente_id INT,
    IN p_nombre VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_fecha_registro DATE
)
BEGIN
    INSERT INTO clientes (cliente_id, nombre, email, fecha_registro)
    VALUES (p_cliente_id, p_nombre, p_email, p_fecha_registro);
END$$

DELIMITER ;

-- Llamar al procedimiento almacenado para insertar un cliente
CALL insertar_cliente(1, 'Juan Pérez', 'juan.perez@ejemplo.com', '2025-04-27');
