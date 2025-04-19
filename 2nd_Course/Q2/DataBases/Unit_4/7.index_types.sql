CREATE TABLE empleados (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- Índice Primario (PRIMARY KEY)
  nombre VARCHAR(100),                -- No tiene índice por defecto
  email VARCHAR(100) UNIQUE,          -- Índice Único (UNIQUE)
  fecha_nacimiento DATE,              -- No tiene índice por defecto
  salario DECIMAL(10, 2),             -- No tiene índice por defecto
  departamento_id INT,                -- No tiene índice por defecto
  INDEX idx_nombre (nombre),          -- Índice Normal (INDEX) en la columna 'nombre'
  INDEX idx_departamento (departamento_id)  -- Índice Normal (INDEX) en la columna 'departamento_id'
);

-- Crear un índice compuesto (varias columnas)
CREATE INDEX idx_email_salario ON empleados (email, salario);

-- Ejemplo de consulta optimizada usando los índices
EXPLAIN SELECT * FROM empleados WHERE email = 'ejemplo@dominio.com' AND salario > 5000;
