--Switch to unix_socket authentication [Y/n] n

--Enter current password for root (enter for none): Just press the Enter

--Set root password? [Y/n]: Y

--New password: Enter password

--Re-enter new password: Repeat password

--Remove anonymous users? [Y/n]: Y

--Disallow root login remotely? [Y/n]: Y

--Remove test database and access to it? [Y/n]: Y

--Reload privilege tables now? [Y/n]: Y


--Create database 

CREATE DATABASE prueba_db;

--create  user 

CREATE USER 'user_prueba'@localhost IDENTIFIED BY'password_de_user_prueba';

--privileges

GRANT ALL PRIVILEGES ON prueba_db.* TO 'user_prueba'@localhost;

--aply changes 

FLUSH PRIVILEGES; 

--QUIT

QUIT

