-- ============================================================
-- Mathematical Functions
-- ============================================================

-- ABS: Returns the absolute value of a number
SELECT ABS(0), ABS(12), ABS(-33);
-- Result: 0, 12, 33

-- CEIL: Returns the smallest integer greater than or equal to the number
SELECT CEIL(2.69);  -- Result: 3
SELECT CEIL(-2.69); -- Result: -2

-- FLOOR: Returns the largest integer less than or equal to the number
SELECT FLOOR(2.69);   -- Result: 2
SELECT FLOOR(-2.69);  -- Result: -3

-- MOD: Returns the remainder of the division between two numbers
SELECT MOD(11, 3);    -- Result: 2
SELECT MOD(11, 0);    -- Result: NULL (division by zero)

-- TRUNCATE: Truncates a number to a specific number of decimal places
SELECT TRUNCATE(1.555, 1);  -- Result: 1.5
SELECT TRUNCATE(199.99, -2); -- Result: 100
SELECT TRUNCATE(1.999, 1);   -- Result: 1.9
SELECT ROUND(1.999, 1);      -- Result: 2.0


-- ============================================================
-- Date and Time Functions
-- ============================================================

-- CURDATE: Returns the current date
SELECT CURDATE();      -- Result: 2023-07-11
SELECT CURDATE() + 0;  -- Result: 20230711

-- DATEDIFF: Returns the number of days between two dates
SELECT DATEDIFF('2022-08-08', '2022-08-28');  -- Result: -20
SELECT DATEDIFF('2022-08-28', '2022-08-20');  -- Result: 8

-- DAY: Returns the day of the month from a date
SELECT DAY('2023-01-15'); -- Result: 15
SELECT DAY('2023-12-31'); -- Result: 31

-- NOW: Returns the current date and time
SELECT NOW();        -- Result: 2023-03-04 10:21:14
SELECT NOW() + 0;    -- Result: 20230304102206

-- MONTH: Returns the month number from a date
SELECT MONTH('2023-03-05'); -- Result: 3

-- YEAR: Returns the year from a date
SELECT YEAR('2023-01-01');  -- Result: 2023
SELECT YEAR(CURDATE());     -- Result: 2023


-- ============================================================
-- Aggregation Functions
-- ============================================================

-- AVG: Returns the average of a set of values
SELECT TRUNCATE(AVG(salary), 2) FROM instructor;

-- MIN: Returns the minimum value from a set of values
SELECT MIN(salary) FROM instructor;

-- MAX: Returns the maximum value from a set of values
SELECT MAX(salary) FROM instructor;

-- SUM: Returns the sum of a set of values
SELECT SUM(salary) FROM instructor WHERE dept_name = 'Finance';
SELECT TRUNCATE(SUM(salary) / 12, 2) FROM instructor WHERE dept_name = 'Finance';

-- COUNT: Counts the number of values
SELECT COUNT(*) FROM instructor;
SELECT COUNT(DISTINCT ID) FROM teaches WHERE semester = 'Spring' AND year = 2018;


-- ============================================================
-- Control Flow Functions
-- ============================================================

-- CASE: Performs conditions within a query
SELECT name, COUNT(course_id) AS num_courses,
    CASE
        WHEN COUNT(course_id) > 4 THEN 'Good professor: more than 4 courses'
        WHEN COUNT(course_id) BETWEEN 2 AND 4 THEN 'Good professor: between 2-4 courses'
        ELSE 'Teaches less than 2 courses'
    END AS result
FROM teaches, instructor
WHERE teaches.ID = instructor.ID
GROUP BY name;

-- IF: Evaluates a simple condition and returns a value based on its result
SELECT title, IF(credits > 3, 'More than 3 credits', '3 credits or less')
FROM course;

-- IFNULL: Returns the first value if it is not NULL, or the second value if the first is NULL
SELECT IFNULL(credits, 0) FROM course;

-- NULLIF: Returns the first value if it is not equal to the second, or NULL if both are equal
SELECT NULLIF(salary, 0) FROM instructor;


-- ============================================================
-- String Functions
-- ============================================================

-- ORD: Returns the ASCII code of a character
SELECT ORD('A'); -- Result: 65

-- CHAR: Returns the characters corresponding to the provided ASCII codes
SELECT CHAR(65, 66, 67); -- Result: 'ABC'

-- CONCAT: Concatenates two or more strings
SELECT CONCAT('Good morning, ', '--', 'INSD'); -- Result: 'Good morning, --INSD'

-- FIND_IN_SET: Searches for a string within a comma-separated list
SELECT FIND_IN_SET('Hello', 'How is Raul, Hello, Good morning'); -- Result: 2

-- LENGTH: Returns the length of a string
SELECT LENGTH('Good morning INSD'); -- Result: 18

-- INSTR: Returns the position of the first occurrence of a substring in a string
SELECT INSTR('Good morning', 'os'); -- Result: 3

-- LEFT / RIGHT: Returns a substring from the left or right of the original string
SELECT LEFT('Good morning INSD', 8); -- Result: 'Good mor'
SELECT RIGHT('Good morning INSD', 8); -- Result: 'ng INSD'

-- SUBSTRING: Extracts a substring from a string starting at a specific position
SELECT SUBSTRING('Good afternoon', 3, 5); -- Result: 'od af'


-- ============================================================
-- Query Types
-- ============================================================

-- Simple Queries: Retrieve data from a single table
SELECT name, age FROM employees WHERE age > 30;

-- Grouped Queries: Group rows and apply aggregation functions
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- Multi-table Queries (JOIN): Combine data from multiple tables
SELECT employees.name, departments.name AS department
FROM employees
JOIN departments ON employees.department_id = departments.id;

-- Nested Queries: Queries within other queries
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Set Queries (UNION, INTERSECT, EXCEPT): Combine results from multiple SELECT statements
-- UNION: Combines results without duplicates
SELECT name FROM employees_madrid
UNION
SELECT name FROM employees_barcelona;

-- INTERSECT: Returns common results between two queries
SELECT name FROM employees_madrid
INTERSECT
SELECT name FROM employees_barcelona;

-- EXCEPT: Returns results from the first query that are not in the second
SELECT name FROM employees_madrid
EXCEPT
SELECT name FROM employees_barcelona;

-- Queries with CTE (WITH): Temporary reusable queries within the same query
WITH older_employees AS (
    SELECT name, age FROM employees WHERE age > 40
)
SELECT * FROM older_employees;


-- ============================================================
-- Data Update Operations
-- ============================================================

-- INSERT: Insert new records into a table
-- Insert direct values
INSERT INTO course VALUES ('HH-888', 'AI', 'Comp. Sci.', 2);

-- Insert specific values into columns
INSERT INTO course (course_id, title, dept_name, credits)
VALUES ('HT-999', 'ChatGPT', 'Comp. Sci.', 4);

-- Insert data with SELECT
INSERT INTO instructor
SELECT ID+100, 'Carlos Resino', dept_name, 33000.34
FROM student;