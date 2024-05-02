------------------ INSERT ------------------------------------------------------

CREATE TABLE IF NOT EXISTS app_trace ( --create test database

     trace_id BIGINT AUTO_INCREMENT,

     app_name VARCHAR(100) NOT NULL,

     environment VARCHAR(100) NOT NULL,

    area VARCHAR(20) NOT NULL,

     project VARCHAR(100) NOT NULL,

    tstamp DATETIME NOT NULL DEFAULT NOW(),

    error VARCHAR(9) DEFAULT 'NO_ERROR',

    comments TEXT,

    PRIMARY KEY (trace_id)

);

-- Insert values in a row 

INSERT INTO app_trace(app_name, environment, area, project) -- rows

VALUES('gtfsCleaner', 'QA', 'DE', 'lisboa'); -- values 

-- Insert default values 

INSERT INTO app_trace(app_name, environment, area, project, tstamp, error)

VALUES('gtfsLoader', 'QA', 'DE', 'lisboa', DEFAULT, DEFAULT);

-- Insert values with dates 

INSERT INTO app_trace(app_name, environment, area, project, tstamp)

VALUES('gtfsCleaner', 'DEV', 'DE', 'lisboa', '2020-03-02 20:14:53');

-- You can also use functiones for insert date type values in row

INSERT INTO app_trace(app_name, environment, area, project, tstamp)

VALUES('gtfsCleaner', 'DEV', 'DE', 'lisboa', NOW());

-- Insert multiple rows

INSERT INTO 

app_trace(app_name, environment, area, project, error, comments)

VALUES('gtfsLoader', 'PROD', 'DE', 'lisboa', 'WARN', 'Destination directory does not exist, attempting to create it'),
('gtfsLoader', 'PROD', 'DE', 'lisboa', 'ERR', 'Cannot create destination directory: disk full'),
('gtfsLoader', 'PROD', 'DE', 'lisboa', 'FATAL', 'Cannot connect to DB: mob.vehdata.com:3306 (Connection timed out)');

-- UPDATE 

UPDATE app_trace

SET

    comments = 'Manual launch to test error on files', -- values to update 

    tstamp = '2020-03-02 08:14:53'

WHERE

    environment = 'QA' -- conditions

    AND project = 'lisboa'

    AND tstamp = '2020-03-02 20:14:53';

-- update (string replace)

UPDATE app_trace

SET comments = REPLACE(comments, 'error', 'behavior')

WHERE trace_id = 2;

-- Update rows, result select

UPDATE customers 

SET salesRepEmployeeNumber = (

        SELECT employeeNumber

        FROM  employees

        WHERE  jobtitle = 'Sales Rep'

        ORDER BY RAND()

        LIMIT 1)

WHERE

    salesRepEmployeeNumber IS NULL;

-- DELETE 

-- examples

DELETE FROM employees WHERE officeCode= 4;

DELETE FROM customers LIMIT 10;

DELETE FROM customers WHERE country = 'France' ORDER BY creditLimit LIMIT 5;


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