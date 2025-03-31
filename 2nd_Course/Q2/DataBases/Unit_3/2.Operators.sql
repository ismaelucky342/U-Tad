-- Creation of the database and usage
CREATE DATABASE ExampleOperators;
USE ExampleOperators;

-- Creation of a test table
CREATE TABLE Operators (
    id INT PRIMARY KEY AUTO_INCREMENT,
    a INT,
    b INT,
    text1 VARCHAR(20),
    text2 VARCHAR(20)
);

-- Insert test data
INSERT INTO Operators (a, b, text1, text2) VALUES
(10, 3, 'Hello', ' World'),
(25, 5, 'SQL', ' Rocks');

-- 🔢 1️⃣ Arithmetic Operators
SELECT a, b, 
       a + b AS sum, 
       a - b AS subtraction, 
       a * b AS multiplication, 
       a / b AS division, 
       a % b AS modulo
FROM Operators;

-- 🔍 2️⃣ Comparison Operators
SELECT a, b, 
       a = b AS equal, 
       a <> b AS not_equal, 
       a > b AS greater, 
       a < b AS less, 
       a >= b AS greater_or_equal, 
       a <= b AS less_or_equal
FROM Operators;

-- 🟢 3️⃣ Logical Operators
SELECT a, b,
       (a > 5 AND b < 10) AS logical_and, 
       (a > 5 OR b > 10) AS logical_or, 
       NOT (a > 5) AS logical_not
FROM Operators;

-- ⚡ 4️⃣ Bitwise Operators
SELECT a, b,
       a & b AS bitwise_and,
       a | b AS bitwise_or,
       a ^ b AS bitwise_xor,
       ~a AS bitwise_not,
       a << 1 AS shift_left,
       a >> 1 AS shift_right
FROM Operators;

-- 📝 5️⃣ Concatenation Operator (|| in standard SQL, CONCAT in MySQL)
SELECT text1, text2, 
       CONCAT(text1, text2) AS concatenated
FROM Operators;

-- 🔄 6️⃣ Assignment Operator
UPDATE Operators SET a = 50 WHERE id = 1;  -- Assigns a new value to 'a'

-- ✅ Verify the changes
SELECT * FROM Operators;
