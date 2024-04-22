-- 1
SELECT com_autonoma_camping AS 'Comunidad Autónoma', COUNT(*) AS 'Número de Campings'
FROM campings
GROUP BY com_autonoma_camping
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 2
SELECT com_autonoma_camping AS 'Comunidad Autónoma', COUNT(*) AS 'Número de Campings'
FROM campings
GROUP BY com_autonoma_camping;

-- 3
SELECT DISTINCT com_autonoma_camping AS 'Comunidad Autónoma'
FROM campings;

-- 4
SELECT nombre_camping, direccion_camping, categoria_camping, ciudad_camping, com_autonoma_camping
FROM campings
WHERE direccion_camping LIKE '%Carrera del Riu%' AND ciudad_camping = 'Valencia';

-- 5
UPDATE clientes
SET ciudad_cl = (SELECT ciudad_cl FROM clientes WHERE id_cliente = 5)
WHERE id_cliente = 4;

-- 6
INSERT INTO campings (nombre_camping, direccion_camping, categoria_camping, ciudad_camping, com_autonoma_camping)
VALUES ('Mahon', 'Avenida de las islas baleares, 23', 2, 'Mallorca', 'Islas Baleares');

-- 7
SELECT campings.nombre_camping, parcelas.tipo_parcela, parcelas.num_parcela
FROM campings
INNER JOIN parcelas ON campings.id_camping = parcelas.id_camping_par;

-- 8
SELECT num_parcela, precio, tipo_parcela
FROM parcelas
WHERE num_parcela IN (
    SELECT num_parcela_res
    FROM reservas
    GROUP BY num_parcela_res
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- 9
SELECT campings.nombre_camping, campings.ciudad_camping
FROM campings
INNER JOIN opiniones ON campings.id_camping = opiniones.id_camping_op
GROUP BY campings.id_camping
ORDER BY AVG(valoracion_general) DESC
LIMIT 1;

-- 10
SELECT clientes.nombre_cliente, opiniones.valoracion_general
FROM clientes
INNER JOIN opiniones ON clientes.id_cliente = opiniones.id_cliente_op
WHERE opiniones.valoracion_general = (
    SELECT MAX(valoracion_general)
    FROM opiniones
);

-- 11
SELECT nombre_camping, COUNT(*) AS 'Número de Trabajadores'
FROM campings
INNER JOIN empleados ON campings.id_camping = empleados.id_camping_em
GROUP BY campings.id_camping
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT nombre_camping, COUNT(*) AS 'Número de Trabajadores'
FROM campings
INNER JOIN empleados ON campings.id_camping = empleados.id_camping_em
GROUP BY campings.id_camping
ORDER BY COUNT(*) ASC
LIMIT 1;

-- 12
SELECT num_parcela_res AS 'Número de Parcela', SUM(dias_estancia) AS 'Total de Días Ocupados'
FROM reservas
INNER JOIN parcelas ON reservas.num_parcela_res = parcelas.num_parcela
WHERE tipo_parcela = 'bungalow'
GROUP BY num_parcela_res
ORDER BY SUM(dias_estancia) DESC
LIMIT 1;

-- 13
SELECT clientes.nombre_cliente, clientes.DNI_cliente, clientes.ciudad_cl
FROM clientes
INNER JOIN reservas ON clientes.id_cliente = reservas.id_cliente_res
WHERE reservas.numero_tarjeta = 4241747307190923;

-- 14
SELECT campings.nombre_camping, empleados.nombre_empleado, LENGTH(empleados.nombre_empleado) AS 'Longitud del Nombre'
FROM campings
INNER JOIN empleados ON campings.id_camping = empleados.id_camping_em
ORDER BY LENGTH(empleados.nombre_empleado) DESC
LIMIT 1;

-- 15
SELECT tipo_empleo, COUNT(*) AS 'Número de Empleados'
FROM empleados
GROUP BY tipo_empleo;
