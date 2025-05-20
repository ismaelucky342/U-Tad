-- Ejemplo 1: "Obtener el nombre y el salario de todos los empleados cuyo salario sea mayor a 3000."

SELECT nombre, salario 
FROM empleados 
WHERE salario > 3000;

-- Ejemplo 2: "Contar el número de productos en cada categoría."

SELECT categoría, COUNT(*) AS total_productos
FROM productos
GROUP BY categoría; 

--Ejemplo 3: "Listar los nombres de empleados que trabajan en el departamento 5."

SELECT nombre 
FROM empleados 
WHERE departamento_id = 5; 

--Ejemplo 4: "Obtener la suma total de ventas por cliente."

SELECT cliente_id, SUM(total_ventas) AS total_ventas 
FROM ventas
GROUP BY cliente_id;

-- Ejemplo 5: "Mostrar los productos cuyo stock es menor a 10."

SELECT nombre, stock
FROM productos
WHERE stock < 10;

-- Ejemplo 6: "Obtener el salario promedio por departamento."

SELECT departamento_id, AVG(salario) AS salario_promedio
FROM empleados
GROUP BY departamento_id;

-- Ejemplo 7: "Listar los clientes que no han realizado ninguna compra."

SELECT c.cliente_id, c.nombre
FROM clientes c
LEFT JOIN ventas v ON c.cliente_id = v.cliente_id
WHERE v.venta_id IS NULL;

-- Ejemplo 8: "Mostrar los empleados ordenados por salario descendente."

SELECT nombre, salario
FROM empleados
ORDER BY salario DESC;

-- Ejemplo 9: "Contar el número de empleados por departamento."
SELECT departamento_id, COUNT(*) AS total_empleados
FROM empleados
GROUP BY departamento_id;

-- Ejemplo 10: "Obtener la fecha de la última venta por cliente."
SELECT cliente_id, MAX(fecha_venta) AS ultima_venta
FROM ventas
GROUP BY cliente_id;

-- Ejemplo 11: "Listar los productos que no tienen stock."
SELECT nombre
FROM productos
WHERE stock = 0;

-- Ejemplo 12: "Mostrar los empleados que tienen un salario mayor al promedio de su departamento."
SELECT e.nombre, e.salario
FROM empleados e
JOIN (
	SELECT departamento_id, AVG(salario) AS salario_promedio
	FROM empleados
	GROUP BY departamento_id
) d ON e.departamento_id = d.departamento_id
WHERE e.salario > d.salario_promedio;

-- Ejemplo 13: "Contar el número de ventas por mes."
SELECT MONTH(fecha_venta) AS mes, COUNT(*) AS total_ventas
FROM ventas
GROUP BY mes;
	
-- Ejemplo 14: "Listar los productos que tienen un precio mayor al promedio."
SELECT nombre
FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos);

-- Ejemplo 15: "Mostrar los empleados que no tienen asignaciones."
SELECT e.nombre
FROM empleados e
LEFT JOIN asignaciones a ON e.empleado_id = a.empleado_id
WHERE a.asignacion_id IS NULL;