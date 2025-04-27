-- Crear una tabla de productos
CREATE TABLE productos (
    producto_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Crear el procedimiento para agregar un nuevo producto
DELIMITER $$

CREATE PROCEDURE agregar_producto (
    IN p_producto_id INT,
    IN p_nombre VARCHAR(100),
    IN p_precio DECIMAL(10,2),
    IN p_stock INT
)
BEGIN
    -- Verificar si el producto ya existe
    IF EXISTS (SELECT 1 FROM productos WHERE producto_id = p_producto_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El producto ya existe';
    END IF;

    -- Insertar el nuevo producto
    INSERT INTO productos (producto_id, nombre, precio, stock)
    VALUES (p_producto_id, p_nombre, p_precio, p_stock);
END$$

DELIMITER ;

-- Llamar al procedimiento para agregar un producto
CALL agregar_producto(1, 'Laptop', 1000.00, 10);
