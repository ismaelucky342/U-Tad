-- Ejercicio 1: Transferencia de dinero entre cuentas
START TRANSACTION;
UPDATE cuentas SET saldo = saldo - 100 WHERE id_cuenta = 1;
UPDATE cuentas SET saldo = saldo + 100 WHERE id_cuenta = 2;
COMMIT;

-- Ejercicio 2: Insertar un pedido y sus detalles
START TRANSACTION;
INSERT INTO pedidos (id_cliente, fecha) VALUES (5, NOW());
SET @id_pedido = LAST_INSERT_ID();
INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad) VALUES (@id_pedido, 3, 2);
INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad) VALUES (@id_pedido, 7, 1);
COMMIT;

-- Ejercicio 3: Cancelar una transacción si hay error
START TRANSACTION;
UPDATE productos SET stock = stock - 5 WHERE id_producto = 10;
UPDATE productos SET stock = stock + 5 WHERE id_producto = 20;
-- Si ocurre un error, deshacer cambios
ROLLBACK;

-- Ejercicio 4: Bloqueo de filas para evitar inconsistencias
START TRANSACTION;
SELECT saldo FROM cuentas WHERE id_cuenta = 1 FOR UPDATE;
UPDATE cuentas SET saldo = saldo - 50 WHERE id_cuenta = 1;
COMMIT;

-- Ejercicio 5: Transferencia con comprobación y rollback si saldo insuficiente
START TRANSACTION;
SELECT saldo INTO @saldo FROM cuentas WHERE id_cuenta = 3 FOR UPDATE;
IF @saldo >= 200 THEN
	UPDATE cuentas SET saldo = saldo - 200 WHERE id_cuenta = 3;
	UPDATE cuentas SET saldo = saldo + 200 WHERE id_cuenta = 4;
	COMMIT;
ELSE
	ROLLBACK;
END IF;

-- Ejercicio 6: Insertar cliente y pedido, rollback si el cliente ya existe
START TRANSACTION;
INSERT INTO clientes (nombre, email) VALUES ('Nuevo Cliente', 'nuevo@email.com');
SET @id_cliente = LAST_INSERT_ID();
INSERT INTO pedidos (id_cliente, fecha) VALUES (@id_cliente, NOW());
-- Si ocurre un error (por ejemplo, cliente ya existe), deshacer cambios
ROLLBACK;

-- Ejercicio 7: Uso de SAVEPOINT para control parcial de transacciones
START TRANSACTION;
UPDATE cuentas SET saldo = saldo - 30 WHERE id_cuenta = 5;
SAVEPOINT despues_de_retirar;
UPDATE cuentas SET saldo = saldo + 30 WHERE id_cuenta = 6;
-- Si ocurre un error en el siguiente paso, solo deshacer desde el savepoint
ROLLBACK TO despues_de_retirar;
-- Continúa la transacción o haz más operaciones
COMMIT;

-- Ejercicio 8: Múltiples SAVEPOINTS y liberación
START TRANSACTION;
INSERT INTO productos (nombre, stock) VALUES ('Producto X', 100);
SAVEPOINT despues_de_insertar_producto;
UPDATE productos SET stock = stock + 50 WHERE nombre = 'Producto X';
SAVEPOINT despues_de_actualizar_stock;
-- Si hay un error aquí, deshacer solo la última actualización
ROLLBACK TO despues_de_actualizar_stock;
-- Si todo está bien, liberar savepoints y confirmar
RELEASE SAVEPOINT despues_de_insertar_producto;
RELEASE SAVEPOINT despues_de_actualizar_stock;
COMMIT;