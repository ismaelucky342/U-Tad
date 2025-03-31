-- Show all available databases
SHOW DATABASES;

-- Create a database
CREATE DATABASE my_company;

-- Select a database
USE my_company;

-- Create a table with constraints
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for the employee',
    first_name VARCHAR(100) NOT NULL COMMENT 'First name of the employee',
    last_name VARCHAR(100) NOT NULL COMMENT 'Last name of the employee',
    hire_date DATE NOT NULL COMMENT 'Hire date of the employee',
    salary DECIMAL(10,2) CHECK (salary > 0) COMMENT 'Salary of the employee',
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB;

-- Drop a table if it exists
DROP TABLE IF EXISTS employees;

-- Create a temporary table
CREATE TEMPORARY TABLE temporary_sales (
    sale_id INT PRIMARY KEY,
    total DECIMAL(10,2)
);

-- Insert data into the temporary table
INSERT INTO temporary_sales (sale_id, total)
SELECT sale_id, total FROM sales WHERE sale_date >= '2024-01-01';

-- Manually drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temporary_sales;

-- Modify the structure of a table
ALTER TABLE employees ADD COLUMN email VARCHAR(150);
ALTER TABLE employees DROP COLUMN email;
ALTER TABLE employees MODIFY COLUMN salary DECIMAL(12,2) DEFAULT 3000.00;
ALTER TABLE employees CHANGE COLUMN hire_date start_date DATE;

-- Add and drop foreign keys
ALTER TABLE employees ADD CONSTRAINT FK_employees_departments FOREIGN KEY (department_id) REFERENCES departments(department_id);
ALTER TABLE employees DROP FOREIGN KEY FK_employees_departments;

-- Rename a table
ALTER TABLE employees RENAME TO workers;

-- Truncate a table
TRUNCATE TABLE workers;

-- Add more examples:

-- Create a new table with unique and default constraints
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for the project',
    project_name VARCHAR(200) UNIQUE NOT NULL COMMENT 'Name of the project',
    start_date DATE DEFAULT CURRENT_DATE COMMENT 'Start date of the project',
    budget DECIMAL(15,2) DEFAULT 10000.00 COMMENT 'Budget allocated for the project'
) ENGINE=InnoDB;

-- Add an index to a table
CREATE INDEX idx_project_name ON projects(project_name);

-- Drop an index from a table
DROP INDEX idx_project_name ON projects;

-- Create a view
CREATE VIEW employee_salaries AS
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 5000;

-- Drop a view
DROP VIEW IF EXISTS employee_salaries;

-- Create a stored procedure
DELIMITER //
CREATE PROCEDURE GetHighSalaryEmployees()
BEGIN
    SELECT first_name, last_name, salary
    FROM employees
    WHERE salary > 10000;
END //
DELIMITER ;

-- Call the stored procedure
CALL GetHighSalaryEmployees();

-- Drop the stored procedure
DROP PROCEDURE IF EXISTS GetHighSalaryEmployees;

-- Create a trigger
DELIMITER //
CREATE TRIGGER before_employee_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Salary cannot be negative';
    END IF;
END //
DELIMITER ;

-- Drop the trigger
DROP TRIGGER IF EXISTS before_employee_insert;
