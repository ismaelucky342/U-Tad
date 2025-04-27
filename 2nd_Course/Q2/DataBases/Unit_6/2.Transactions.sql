-- Crear la tabla de cuentas bancarias
CREATE TABLE cuentas_bancarias (
    cuenta_id INT PRIMARY KEY,
    saldo DECIMAL(10,2)
);

-- Crear el procedimiento almacenado para hacer una transferencia
DELIMITER $$

CREATE PROCEDURE transferencia (
    IN p_cuenta_origen INT,
    IN p_cuenta_destino INT,
    IN p_monto DECIMAL(10,2)
)
BEGIN
    DECLARE saldo_origen DECIMAL(10,2);
    DECLARE saldo_destino DECIMAL(10,2);
    
    -- Iniciar la transacción
    START TRANSACTION;

    -- Obtener el saldo de la cuenta de origen
    SELECT saldo INTO saldo_origen FROM cuentas_bancarias WHERE cuenta_id = p_cuenta_origen;
    IF saldo_origen IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cuenta de origen no existe';
    END IF;

    -- Obtener el saldo de la cuenta de destino
    SELECT saldo INTO saldo_destino FROM cuentas_bancarias WHERE cuenta_id = p_cuenta_destino;
    IF saldo_destino IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cuenta de destino no existe';
    END IF;

    -- Verificar si hay suficiente saldo en la cuenta de origen
    IF saldo_origen < p_monto THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Saldo insuficiente en cuenta de origen';
    END IF;

    -- Realizar la transferencia
    UPDATE cuentas_bancarias SET saldo = saldo - p_monto WHERE cuenta_id = p_cuenta_origen;
    UPDATE cuentas_bancarias SET saldo = saldo + p_monto WHERE cuenta_id = p_cuenta_destino;

    -- Confirmar la transacción
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        -- En caso de error, deshacer la transacción
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error en la transferencia';
END$$

DELIMITER ;

-- Llamar al procedimiento de transferencia
CALL transferencia(1, 2, 100.00);
