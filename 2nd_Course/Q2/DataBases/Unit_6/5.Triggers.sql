-- Crear la tabla de auditoría
CREATE TABLE auditoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    accion VARCHAR(100),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear el trigger que audita las inserciones en la tabla clientes
DELIMITER $$

CREATE TRIGGER auditoria_insert_clientes
AFTER INSERT ON clientes
FOR EACH ROW
BEGIN
    INSERT INTO auditoria (accion)
    VALUES (CONCAT('Se insertó un nuevo cliente con ID ', NEW.cliente_id));
END$$

DELIMITER ;

-- Insertar un cliente y verificar la auditoría
INSERT INTO clientes (cliente_id, nombre, email, fecha_registro)
VALUES (2, 'Ana López', 'ana.lopez@ejemplo.com', '2025-04-27');
