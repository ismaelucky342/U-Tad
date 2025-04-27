-- Crear la función para calcular el impuesto sobre ventas
DELIMITER $$

CREATE FUNCTION calcular_impuesto_venta (
    p_monto DECIMAL(10,2),
    p_tasa_impuesto DECIMAL(5,2)
) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE impuesto DECIMAL(10,2);
    
    -- Calcular el impuesto
    SET impuesto = p_monto * (p_tasa_impuesto / 100);
    
    -- Retornar el impuesto calculado
    RETURN impuesto;
END$$

DELIMITER ;

-- Llamar a la función para calcular el impuesto
SELECT calcular_impuesto_venta(1000.00, 15.00);
