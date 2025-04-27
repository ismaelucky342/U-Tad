-- Crear la tabla de transacciones
CREATE TABLE transacciones (
    transaccion_id INT PRIMARY KEY,
    cliente_id INT,
    monto DECIMAL(10,2),
    tipo VARCHAR(50), -- 'debito' o 'credito'
    fecha DATE
);

-- Crear la función para calcular el saldo total de un cliente
DELIMITER $$

CREATE FUNCTION calcular_saldo_total (p_cliente_id INT) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE saldo_total DECIMAL(10,2) DEFAULT 0;
    
    -- Sumar los débitos y los créditos del cliente
    SELECT SUM(CASE WHEN tipo = 'credito' THEN monto ELSE -monto END)
    INTO saldo_total
    FROM transacciones
    WHERE cliente_id = p_cliente_id;
    
    RETURN saldo_total;
END$$

DELIMITER ;

-- Llamar a la función para calcular el saldo total de un cliente
SELECT calcular_saldo_total(1);
