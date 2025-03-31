-- Data Definition Language (DDL) Commands
-- These commands are used to define or modify the structure of the database.

-- Create a new table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Major VARCHAR(50)
);

-- Alter an existing table
ALTER TABLE Students ADD Email VARCHAR(100);

-- Drop a table
DROP TABLE Students;

-- Truncate a table (removes all rows but keeps the structure)
TRUNCATE TABLE Students;


-- Data Manipulation Language (DML) Commands
-- These commands are used to manipulate data in the database.

-- Insert data into a table
INSERT INTO Students (StudentID, Name, Age, Major) 
VALUES (1, 'John Doe', 20, 'Computer Science');

-- Update data in a table
UPDATE Students 
SET Age = 21 
WHERE StudentID = 1;

-- Delete data from a table
DELETE FROM Students 
WHERE StudentID = 1;

-- Select data from a table
SELECT * FROM Students;


-- Data Control Language (DCL) Commands
-- These commands are used to control access to the database.

-- Grant privileges to a user
GRANT SELECT, INSERT ON Students TO 'username';

-- Revoke privileges from a user
REVOKE INSERT ON Students FROM 'username';


-- Transaction Control Language (TCL) Commands
-- These commands are used to manage transactions in the database.

-- Start a transaction
BEGIN TRANSACTION;

-- Commit a transaction
COMMIT;

-- Rollback a transaction
ROLLBACK;

-- Save a transaction point
SAVEPOINT SavePoint1;

-- Rollback to a specific savepoint
ROLLBACK TO SavePoint1;