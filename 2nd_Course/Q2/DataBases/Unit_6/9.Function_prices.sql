-- Crear la tabla de productos
CREATE TABLE productos (
    producto_id INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Crear la tabla de auditoría de precios
CREATE TABLE auditoria_precios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT,
    precio_antiguo DECIMAL(10,2),
    precio_nuevo DECIMAL(10,2),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear el trigger para registrar los cambios de precio
DELIMITER $$

CREATE TRIGGER registrar_cambio_precio
AFTER UPDATE ON productos
FOR EACH ROW
BEGIN
    IF OLD.precio <> NEW.precio THEN
        INSERT INTO auditoria_precios (producto_id, precio_antiguo, precio_nuevo)
        VALUES (NEW.producto_id, OLD.precio, NEW.precio);
    END IF;
END$$

DELIMITER ;

-- Actualizar el precio de un producto para probar el trigger
UPDATE productos SET precio = 1200.00 WHERE producto_id = 1;
