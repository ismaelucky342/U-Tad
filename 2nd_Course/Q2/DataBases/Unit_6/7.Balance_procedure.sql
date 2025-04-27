-- Crear la tabla de cuentas bancarias
CREATE TABLE cuentas_bancarias (
    cuenta_id INT PRIMARY KEY,
    saldo DECIMAL(10,2)
);

-- Crear el procedimiento para actualizar el saldo de una cuenta bancaria
DELIMITER $$

CREATE PROCEDURE actualizar_saldo (
    IN p_cuenta_id INT,
    IN p_monto DECIMAL(10,2)
)
BEGIN
    DECLARE saldo_actual DECIMAL(10,2);

    -- Obtener el saldo actual de la cuenta
    SELECT saldo INTO saldo_actual FROM cuentas_bancarias WHERE cuenta_id = p_cuenta_id;

    -- Verificar que la cuenta exista
    IF saldo_actual IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cuenta no encontrada';
    END IF;

    -- Actualizar el saldo de la cuenta
    UPDATE cuentas_bancarias
    SET saldo = saldo_actual + p_monto
    WHERE cuenta_id = p_cuenta_id;
END$$

DELIMITER ;

-- Llamar al procedimiento para actualizar el saldo de una cuenta
CALL actualizar_saldo(1, 500.00);
