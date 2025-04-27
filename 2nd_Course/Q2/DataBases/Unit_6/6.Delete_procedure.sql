-- Crear la tabla de clientes
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    fecha_registro DATE
);

-- Crear la tabla de transacciones
CREATE TABLE transacciones (
    transaccion_id INT PRIMARY KEY,
    cliente_id INT,
    monto DECIMAL(10,2),
    tipo VARCHAR(50), -- 'debito' o 'credito'
    fecha DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

-- Crear el procedimiento almacenado para eliminar un cliente y sus transacciones
DELIMITER $$

CREATE PROCEDURE eliminar_cliente (
    IN p_cliente_id INT
)
BEGIN
    -- Eliminar las transacciones asociadas al cliente
    DELETE FROM transacciones WHERE cliente_id = p_cliente_id;

    -- Eliminar el cliente
    DELETE FROM clientes WHERE cliente_id = p_cliente_id;
END$$

DELIMITER ;

-- Llamar al procedimiento para eliminar un cliente y sus transacciones
CALL eliminar_cliente(1);
