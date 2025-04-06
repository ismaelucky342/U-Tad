SELECT employees.name AS employee_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;

SELECT employees.name AS employee_name, projects.project_name
FROM employees
LEFT JOIN projects ON employees.department_id = projects.department_id;

SELECT projects.project_name, employees.name AS employee_name
FROM projects
RIGHT JOIN employees ON projects.department_id = employees.department_id;


SELECT employees.name AS employee_name, projects.project_name
FROM employees
LEFT JOIN projects ON employees.department_id = projects.department_id
UNION
SELECT employees.name AS employee_name, projects.project_name
FROM projects
RIGHT JOIN employees ON projects.department_id = employees.department_id;

