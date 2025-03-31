-- ============================================================
-- **Exercise 1: Table Normalization**
-- ============================================================

-- ============================================================
-- **Table COMPRAS**
-- ============================================================

-- **Normalization Analysis**
-- The COMPRAS table has the following functional dependencies:
-- 1. ID_Cliente → nom_cliente, Fecha_nacimiento (A client has a fixed name and birth date).
-- 2. ID_Producto → sección, precio (Each product belongs to a single section and has a price).
-- 3. (ID_Cliente, ID_Producto) → (Complete dependencies).
--
-- **Problem:**
-- - Information about clients and products is unnecessarily repeated.
-- - It is not in 3NF as there are transitive dependencies (e.g., ID_Producto determines sección and precio).
--
-- **Transformation to 3NF:**
-- The tables are divided into:
-- 1. CLIENTES (ID_Cliente, nom_cliente, Fecha_nacimiento)
-- 2. PRODUCTOS (ID_Producto, sección, precio)
-- 3. COMPRAS (ID_Cliente, ID_Producto)

-- **SQL Queries for Table COMPRAS:**
CREATE TABLE CLIENTES (
    ID_Cliente INT PRIMARY KEY,
    nom_cliente VARCHAR(100),
    Fecha_nacimiento DATE
);

CREATE TABLE PRODUCTOS (
    ID_Producto INT PRIMARY KEY,
    sección VARCHAR(50),
    precio DECIMAL(10,2)
);

CREATE TABLE COMPRAS (
    ID_Cliente INT,
    ID_Producto INT,
    PRIMARY KEY (ID_Cliente, ID_Producto),
    FOREIGN KEY (ID_Cliente) REFERENCES CLIENTES(ID_Cliente),
    FOREIGN KEY (ID_Producto) REFERENCES PRODUCTOS(ID_Producto)
);

-- ============================================================
-- **Table ORDEN**
-- ============================================================

-- **Normalization Analysis**
-- The functional dependencies are:
-- 1. DNI_operario → ap1_operario (The operator's last name depends on their DNI).
-- 2. DNI_supervisor → ap1_supervisor (The supervisor's last name depends on their DNI).
-- 3. num_orden → nom_orden, fecha_inicio, fecha_fin (Each order has a name, start date, and end date).
-- 4. (num_orden, DNI_operario) → función (Each operator performs a function in an order).
--
-- **Problem:**
-- - There is redundancy in the information about operators and supervisors.
-- - There are transitive dependencies (e.g., DNI_supervisor determines ap1_supervisor).
--
-- **Transformation to 3NF:**
-- The tables are divided into:
-- 1. OPERARIOS (DNI_operario, ap1_operario)
-- 2. SUPERVISORES (DNI_supervisor, ap1_supervisor)
-- 3. ORDENES (num_orden, nom_orden, fecha_inicio, fecha_fin, DNI_supervisor)
-- 4. ORDEN_OPERARIOS (num_orden, DNI_operario, función)

-- **SQL Queries for Table ORDEN:**
CREATE TABLE OPERARIOS (
    DNI_operario VARCHAR(20) PRIMARY KEY,
    ap1_operario VARCHAR(50)
);

CREATE TABLE SUPERVISORES (
    DNI_supervisor VARCHAR(20) PRIMARY KEY,
    ap1_supervisor VARCHAR(50)
);

CREATE TABLE ORDENES (
    num_orden INT PRIMARY KEY,
    nom_orden VARCHAR(100),
    fecha_inicio DATE,
    fecha_fin DATE,
    DNI_supervisor VARCHAR(20),
    FOREIGN KEY (DNI_supervisor) REFERENCES SUPERVISORES(DNI_supervisor)
);

CREATE TABLE ORDEN_OPERARIOS (
    num_orden INT,
    DNI_operario VARCHAR(20),
    función VARCHAR(50),
    PRIMARY KEY (num_orden, DNI_operario),
    FOREIGN KEY (num_orden) REFERENCES ORDENES(num_orden),
    FOREIGN KEY (DNI_operario) REFERENCES OPERARIOS(DNI_operario)
);

-- ============================================================
-- **Explanation of the Normalization Process:**
-- For the COMPRAS table, we split the data into CLIENTES, PRODUCTOS, and COMPRAS tables, 
-- each holding only the necessary information and eliminating redundancy.
--
-- For the ORDEN table, the data is normalized by creating separate tables for 
-- OPERARIOS, SUPERVISORES, and ORDENES, and we manage the relationship between 
-- operators and orders using the ORDEN_OPERARIOS table. This helps eliminate 
-- redundant information and satisfies the 3NF.
