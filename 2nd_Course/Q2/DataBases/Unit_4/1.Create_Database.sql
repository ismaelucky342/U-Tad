-- 1. Crear la base de datos
CREATE DATABASE tienda_online;
USE tienda_online;

-- 2. Crear las tablas
CREATE TABLE CLIENTES (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100) UNIQUE
) ENGINE=InnoDB;

CREATE TABLE PRODUCTOS (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  precio DECIMAL(10,2),
  stock INT
);

CREATE TABLE VENTAS (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  producto_id INT,
  fecha DATE,
  cantidad INT,
  FOREIGN KEY (cliente_id) REFERENCES CLIENTES(id),
  FOREIGN KEY (producto_id) REFERENCES PRODUCTOS(id)
) ENGINE=MyISAM;

-- 3. Índices
CREATE INDEX idx_nombre ON PRODUCTOS(nombre);
CREATE INDEX idx_cliente_fecha ON VENTAS(cliente_id, fecha);

-- 4. Particionamiento por rango (requiere eliminar claves foráneas y usar ENGINE=InnoDB)
-- Creamos una tabla sin claves foráneas para particionar
DROP TABLE IF EXISTS VENTAS;
CREATE TABLE VENTAS (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  producto_id INT,
  fecha DATE,
  cantidad INT
)
PARTITION BY RANGE (YEAR(fecha)) (
  PARTITION p0 VALUES LESS THAN (2021),
  PARTITION p1 VALUES LESS THAN (2022),
  PARTITION p2 VALUES LESS THAN MAXVALUE
);

-- 5. Consulta optimizada
EXPLAIN SELECT * FROM VENTAS
WHERE cliente_id = 5 AND fecha BETWEEN '2021-01-01' AND '2022-12-31';
