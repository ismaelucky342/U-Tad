
--restore database 

mysql -u [user] -p [name_db] < [path/name_file].sql 

-- SELECT query 

SELECT * FROM Client; 

-- Another SELECT query 

SELECT name_cl, salary_cl FROM Client; 

-- Operators 

--WHERE 

SELECT nombre_cl, ciudad_cl, pais_cl 

FROM Cliente 

WHERE pais_cl = 'Francia' AND ciudad_cl = 'Paris';

--ORDER BY 

SELECT nombre_cl, ciudad_cl 

FROM CLiente 

ORDER BY nombre_cl;

--LIMIT 

SELECT nombre_cl, direccion_cl, saldo_cl 

FROM Cliente 

ORDER BY saldo_cl DESC LIMIT 5;

--DISTINCT 

SELECT DISTINCT ciudad_cl 

FROM Cliente ORDER BY ciudad_cl;

--GROUP BY 

SELECT name_column FROM name_table WHERE condition  

GROUP BY name_column;  

--Additional functions 

--Get how many items each supplier provides, grouped by supplier ID and ordered by the number of items from highest to lowest.

SELECT
    id_supplier_warehouse, 
    COUNT(*)
FROM
    warehouse
GROUP BY
    id_supplier_warehouse
ORDER BY
    COUNT(*) DESC;

-- Obtain the total value of items supplied by each supplier. Assign this quantity an alias using the AS clause. The result should be grouped by supplier.

SELECT
    id_supplier_warehouse,
    SUM(item_stock_warehouse * unit_price) AS total
FROM
    warehouse
GROUP BY
    id_supplier_warehouse;

-- Get the average price of all items in the warehouse (returns a single row).

SELECT
    AVG(unit_price)
FROM
    warehouse;

-- Now select the average unit price of each item, but grouped by supplier and ordered by the average value from highest to lowest.

SELECT
    id_supplier_warehouse,
    id_item_warehouse,
    AVG(unit_price) as average
FROM
    warehouse
GROUP BY
    id_supplier_warehouse
ORDER BY
    average DESC;


-- Select the total number of items in the warehouse grouped by supplier identifier. Note that the COUNT clause can be placed as part of the ORDER BY clause.

SELECT
    id_supplier_warehouse,
    COUNT(*)
FROM
    warehouse
GROUP BY
    id_supplier_warehouse
ORDER BY
    COUNT(*) DESC;


-- DATE functions 

NOW():-- Returns a constant indicating the point in time (date and time) when the statement begins execution.

SYSDATE(): -- Returns the date and time from the server at the moment the function is executed. This differs from NOW(). If the NOW() function is executed multiple times within the same statement, it will always return the same value. This is not the case with SYSDATE(), which returns the date each time it is executed.

CURRENT_DATE(): -- Returns the current date of the client. If the server and the client are on the same machine, there will be no difference.

DATE_ADD('Date', INTERVAL <num> MINUTE): -- Adds the specified number of minutes to the date value indicated in the interval.

DATE_ADD('Date', INTERVAL <num> HOUR): -- Adds the specified number of hours to the date value indicated in the interval.

DATE_ADD('Date', INTERVAL <num> DAY): -- Adds the specified number of days to the date value indicated in the interval.

DATE_SUB('Date', Interval <num> MIN/DAY/HOUR): -- Subtracts the specified value in the interval from a date.

-- To compare dates, we will use the operators: >, <, <=, and >=.

-- STRING functions 

-- LOWER or LCASE converts a string to lowercase:

SELECT LOWER('Hello'); ⇒ hello

--UPPER or UCASE converts a string to uppercase:

SELECT UPPER('Hello'); ⇒ HELLO


--LEFT(string, length) extracts multiple characters from the beginning (the left part) of the string:

SELECT LEFT('Hello', 2); ⇒ He


-- RIGHT(string, length) extracts multiple characters from the end (the right part) of the string:

SELECT RIGHT('Hello', 2); ⇒ lo


-- CONCAT joins (concatenates) multiple strings to form a new one:

SELECT CONCAT('Hel', 'lo'); ⇒ Hello

-- REPLACE(string, old substring, new substring) returns the string by replacing certain sequences of characters with others:

SELECT REPLACE('Hello', 'l', 'LL'); ⇒ HeLLLo

-- LENGTH returns the length of the string:

SELECT LENGTH('Hello'); ⇒ 5





