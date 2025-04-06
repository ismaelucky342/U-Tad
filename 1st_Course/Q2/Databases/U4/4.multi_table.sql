-- Insertar departamentos
INSERT INTO departments (department_name) VALUES 
('HR'), 
('IT'), 
('Marketing');

-- Insertar empleados
INSERT INTO employees (name, department_id, hire_date, salary) VALUES 
('Alice', 1, '2015-04-23', 55000.00),
('Bob', 2, '2017-08-15', 60000.00),
('Charlie', 3, '2019-11-11', 45000.00),
('David', 2, '2020-03-20', 70000.00);

-- Insertar proyectos
INSERT INTO projects (project_name, department_id, start_date, end_date) VALUES
('HR Automation', 1, '2021-01-01', '2022-01-01'),
('Web Development', 2, '2021-06-15', '2023-06-15'),
('Digital Marketing Campaign', 3, '2021-09-01', '2022-09-01');

-- Insertar salarios históricos
INSERT INTO salaries (employee_id, salary, start_date, end_date) VALUES
(1, 55000.00, '2015-04-23', '2020-04-22'),
(2, 60000.00, '2017-08-15', '2022-08-15'),
(3, 45000.00, '2019-11-11', '2021-11-11');

-- Insertar registros de asistencia
INSERT INTO attendance (employee_id, date, status) VALUES
(1, '2021-12-01', 'Present'),
(1, '2021-12-02', 'Absent'),
(2, '2021-12-01', 'Present'),
(2, '2021-12-02', 'Present'),
(3, '2021-12-01', 'Present'),
(4, '2021-12-01', 'Absent');
