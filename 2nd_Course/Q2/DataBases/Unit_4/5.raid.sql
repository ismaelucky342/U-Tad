-- Crear base de datos
CREATE DATABASE logs_empresa;
USE logs_empresa;

-- Tabla para almacenar logs del sistema
CREATE TABLE LOGS (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario VARCHAR(50),
  accion TEXT,
  fecha DATETIME NOT NULL
)
PARTITION BY RANGE (YEAR(fecha)) (
  PARTITION p2021 VALUES LESS THAN (2022),
  PARTITION p2022 VALUES LESS THAN (2023),
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION pmax VALUES LESS THAN MAXVALUE
);

-- Crear índice para mejorar búsqueda por usuario y fecha
CREATE INDEX idx_usuario_fecha ON LOGS(usuario, fecha);

-- Consulta típica optimizada
EXPLAIN SELECT * FROM LOGS
WHERE usuario = 'admin' AND fecha BETWEEN '2022-01-01' AND '2022-12-31';
