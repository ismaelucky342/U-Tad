-- DDL (Data Definition Language): Create a table
CREATE TABLE Employees (
    ID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255)
);

-- DML (Data Manipulation Language): Query data
SELECT ProductCode, Product FROM Products;

-- Additional example of DDL: Modify a table
ALTER TABLE Employees ADD BirthDate DATE;

-- Additional example of DDL: Drop a table
DROP TABLE Employees;

-- Additional example of DML: Insert data
INSERT INTO Employees (ID, LastName, FirstName, Address) 
VALUES (1, 'Garcia', 'Juan', 'Fake Street 123');

-- Additional example of DML: Update data
UPDATE Employees 
SET Address = 'True Street 456' 
WHERE ID = 1;

-- Additional example of DML: Delete data
DELETE FROM Employees 
WHERE ID = 1;