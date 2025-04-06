-- JOIN

-- 1. INNER JOIN

-- Select employee names and their department names
SELECT employees.name, departments.department_name
FROM employees
-- Joining employees table with departments table based on department_id
INNER JOIN departments ON employees.department_id = departments.department_id;

-- 2. LEFT JOIN

-- Select employee names and their department names
SELECT employees.name, departments.department_name
FROM employees
-- Left join employees table with departments table based on department_id
LEFT JOIN departments ON employees.department_id = departments.department_id;

-- 3. RIGHT JOIN

-- Select employee names and their department names
SELECT employees.name, departments.department_name
FROM employees
-- Right join employees table with departments table based on department_id
RIGHT JOIN departments ON employees.department_id = departments.department_id;

-- 4. FULL JOIN

-- Select employee names and their department names
SELECT employees.name, departments.department_name
FROM employees
-- Full outer join employees table with departments table based on department_id
FULL JOIN departments ON employees.department_id = departments.department_id;


-- VIEWS

CREATE VIEW vista_alumnos AS SELECT * FROM alumnos;

-- or

CREATE VIEW vista_alumnos AS 

SELECT alumnos.id, nombre, grado FROM alumnos

WHERE edad < 15;


