-- Creation of the CLIENTES, LOCALIDADES, and FACTURAS tables with integrity constraints

-- CLIENTES Table
CREATE TABLE CLIENTES (
    codCliente INT PRIMARY KEY, -- Primary key, cannot be null
    nombreCliente VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    codLocalidad INT, -- Foreign key referencing LOCALIDADES
    FOREIGN KEY (codLocalidad) REFERENCES LOCALIDADES(codLocalidad)
);

-- LOCALIDADES Table
CREATE TABLE LOCALIDADES (
    codLocalidad INT PRIMARY KEY, -- Primary key, cannot be null
    nombreLocalidad VARCHAR(100) NOT NULL
);

-- FACTURAS Table
CREATE TABLE FACTURAS (
    codFactura INT PRIMARY KEY, -- Primary key, cannot be null
    fecha DATE NOT NULL,
    codCliente INT, -- Foreign key referencing CLIENTES
    FOREIGN KEY (codCliente) REFERENCES CLIENTES(codCliente)
        ON DELETE SET NULL -- Deletion rule: Set to NULL (sets the foreign key to NULL)
        ON UPDATE CASCADE -- Update rule: Cascade (updates the foreign key)
);

-- Example of data insertion
INSERT INTO LOCALIDADES (codLocalidad, nombreLocalidad) VALUES (1, 'Madrid');
INSERT INTO CLIENTES (codCliente, nombreCliente, direccion, codLocalidad) VALUES (101, 'Juan Pérez', 'Calle Mayor 1', 1);
INSERT INTO FACTURAS (codFactura, fecha, codCliente) VALUES (1001, '2023-01-01', 101);

-- Example of deleting a client
-- DELETE FROM CLIENTES WHERE codCliente = 101;

-- Example of updating a client's code
-- UPDATE CLIENTES SET codCliente = 102 WHERE codCliente = 101;