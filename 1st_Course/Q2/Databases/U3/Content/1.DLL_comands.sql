--Create database
mysql -u [user] -p

mysql> CREATE DATABASE testdb;


mysql> SHOW CREATE DATABASE testdb;


mysql> SHOW databases;


mysql> USE testdb;

--Drop database

mysql> DROP DATABASE testdb;

--cretate table

CREATE TABLE table_name (column1_def, column2_def..., table_constraints) 


--Drop table 

DROP TABLE table_name, table2; 


------------------------USER SQL----------------------------------------------------------------

-- Create user 

CREATE USER name_account IDENTIFIED 'PSWD';

-- Grant all privileges

GRANT ALL PRIVILEGES ON name_bd.* TO user_name@hostname; 

-- update 

FLUSH PRIVILEGES; 

-- Show changes 

SHOW GRANTS FOR user_name@hostname; 

-- Drop user 

DROP USER name_account;



