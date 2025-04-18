-- Escenario 1: Evitar el uso de SELECT * y seleccionar solo los campos necesarios
SELECT id, nombre, email FROM users WHERE age > 30;

-- Escenario 2: Usar índices para mejorar las consultas en tablas grandes
CREATE INDEX idx_age ON users(age);

-- Escenario 3: Evitar subconsultas en WHERE y usar JOIN
SELECT users.name, orders.amount 
FROM users 
JOIN orders ON users.id = orders.user_id 
WHERE orders.date > '2023-01-01';

-- Escenario 4: Usar EXPLAIN para analizar el rendimiento de las consultas
EXPLAIN SELECT * FROM users WHERE age > 30;

-- Escenario 5: Consultas con LIMIT para reducir el tamaño de la respuesta
SELECT * FROM users LIMIT 100;
