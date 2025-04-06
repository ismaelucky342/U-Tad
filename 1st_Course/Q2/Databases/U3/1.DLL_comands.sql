--Create database (create, show and use a database)
mysql -u [user] -p

mysql> CREATE DATABASE testdb;


mysql> SHOW CREATE DATABASE testdb;


mysql> SHOW databases;


mysql> USE testdb;

--Drop database (destroy tables and databases)

mysql> DROP DATABASE testdb;

--cretate table (create tables in the DB)

CREATE TABLE table_name (column1_def, column2_def..., table_constraints) 

-- example: 
CREATE TABLE IF NOT EXISTS tasks (

    task_id INT AUTO_INCREMENT PRIMARY KEY, -- column task_id as PK

    title VARCHAR(255) NOT NULL, -- title not null with 255 char max 

    start_date DATE, -- start date

    due_date DATE, -- due date

    status TINYINT NOT NULL, -- TINYINT int type with less space, 

    priority TINYINT NOT NULL, -- priority 

    description TEXT, -- description 

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- records date and time,  timestamp type
);

CREATE TABLE IF NOT EXISTS CHECKLIST (  -- create table checklist 

    todo_id INT AUTO_INCREMENT, -- column int (number) that increases automatically on each record

    task_id INT, -- int, link with other tables

    todo VARCHAR(255) NOT NULL, -- text of task

    is_completed BOOLEAN NOT NULL DEFAULT FALSE, -- true or false, but default false 

    PRIMARY KEY (todo_id , task_id), -- first 2 columns are PK

    FOREIGN KEY (task_id) REFERENCES tasks (task_id) ON UPDATE RESTRICT ON DELETE CASCADE 

);

-- Describe table 

DESC table_example; 

--Drop table (destroy tables)

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



