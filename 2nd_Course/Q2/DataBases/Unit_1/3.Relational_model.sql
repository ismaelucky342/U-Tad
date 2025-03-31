-- Crear tabla Clientes
CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Crear tabla Pedidos con clave foránea
CREATE TABLE Pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES Clientes(id) ON DELETE CASCADE,
    producto VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL
);

-- Insertar datos
INSERT INTO Clientes (nombre, email) VALUES ('Juan Pérez', 'juan@email.com');
INSERT INTO Pedidos (cliente_id, producto, cantidad) VALUES (1, 'Laptop', 1);

-- Consulta para obtener pedidos con información del cliente
SELECT Clientes.nombre, Pedidos.producto, Pedidos.cantidad
FROM Clientes
JOIN Pedidos ON Clientes.id = Pedidos.cliente_id;
