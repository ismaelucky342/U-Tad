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

