## Introduction

To tackle this task, I used a combination of tools and methodologies that allowed me to structure the work efficiently and systematically. The text editor **Notion** was key for documenting each step and organizing the work, enabling the incorporation of code directly into the document in a visually appealing way and facilitating subsequent PDF conversion. Additionally, a **virtual machine with Ubuntu 24** was used to develop and test SQL queries in a real environment. **pgAdmin** was also crucial for managing the database and verifying the correct implementation of the queries.

The objective of the task is to **design, normalize, and implement relational databases**, ensuring compliance with normalization rules (up to the **Third Normal Form**) and executing queries in **Relational Algebra (RA) and SQL**.

The activity is distributed as follows:

- **Exercise 1: Table Normalization:** Analyzing a table with redundancy and unnecessary dependencies. Applying normalization rules to decompose it into more efficient structures up to **3NF**.
- **Exercise 2: Transformation of the Entity-Relationship Model:** Transforming an **Entity-Relationship (E-R)** diagram into a relational model in SQL, ensuring the correct representation of entities, relationships, and constraints.
- **Exercise 3: Database Creation and SQL Queries:** Implementing the relational model in **PostgreSQL**, creating the database, inserting test data, and executing optimized SQL queries.
- **Exercise 4: Relational Algebra (RA) Expressions:** Formulating **Relational Algebra** expressions to extract key information using operators such as **selection (σ), projection (π), natural join (⨝), aggregation (γ), and Cartesian product (×)**.

## **Exercise 1: Table Normalization**

### **Table COMPRAS**

### **Normalization Analysis**

The COMPRAS table has the following functional dependencies:

- **ID_Cliente** → **nom_cliente, Fecha_nacimiento** (A client has a fixed name and birth date).
- **ID_Producto** → **sección, precio** (Each product belongs to a single section and has a price).
- **(ID_Cliente, ID_Producto)** → (Complete dependencies).

### **Problem:**

- Information about clients and products is unnecessarily repeated.
- It is not in 3NF as there are transitive dependencies (e.g., **ID_Producto** determines **sección** and **precio**).

### **Transformation to 3NF:**

The tables are divided into:

1. **CLIENTES (ID_Cliente, nom_cliente, Fecha_nacimiento)**
2. **PRODUCTOS (ID_Producto, sección, precio)**
3. **COMPRAS (ID_Cliente, ID_Producto)**

### **SQL Queries:**

```sql
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
```

### **Explanation:**

- I separated the information about clients and products into individual tables, and the COMPRAS table now only contains foreign keys, eliminating redundancy.

---

### **Table ORDEN**

### **Normalization Analysis**

The functional dependencies are:

- **DNI_operario** → **ap1_operario** (The operator's last name depends on their DNI).
- **DNI_supervisor** → **ap1_supervisor** (The supervisor's last name depends on their DNI).
- **num_orden** → **nom_orden, fecha_inicio, fecha_fin** (Each order has a name, start date, and end date).
- **(num_orden, DNI_operario)** → **función** (Each operator performs a function in an order).

### **Problem:**

- There is redundancy in the information about operators and supervisors.
- There are transitive dependencies (e.g., **DNI_supervisor** determines **ap1_supervisor**).

### **Transformation to 3NF:**

The tables are divided into:

1. **OPERARIOS (DNI_operario, ap1_operario)**
2. **SUPERVISORES (DNI_supervisor, ap1_supervisor)**
3. **ORDENES (num_orden, nom_orden, fecha_inicio, fecha_fin, DNI_supervisor)**
4. **ORDEN_OPERARIOS (num_orden, DNI_operario, función)**

### **SQL Queries:**

```sql
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
```

### **Explanation:**

I separated the information about operators and supervisors. The relationship between operators and orders is managed in an intermediate table, eliminating data redundancy.

## **Exercise 2: Transformation of the E-R Model**

A partir del diagrama entidad-relación proporcionado, he realizado la transformación al modelo relacional.

### **Entidades y Atributos**

En el modelo E-R, identificamos tres entidades principales:

1. **Médico**
    - Atributos: `dni`, `numColegiado`, `nombre`
2. **Paciente**
    - Atributos: `dni`, `numSegSocial`, `nombre`
3. **Análisis**
    - Atributos: `analisisID`, `fecha`, `parametro`, `valor`

### **Relaciones y sus Cardinalidades**

El diagrama muestra tres relaciones importantes:

1. **Atiende (Médico ⇄ Paciente)** → Relación **N:M**
    - Un médico puede atender a varios pacientes, y un paciente puede ser atendido por varios médicos.
    - Creo una tabla intermedia para gestionar esta relación.
2. **Solicita (Médico ⇄ Análisis)** → Relación **1:N**
    - Un médico solicita muchos análisis, pero cada análisis es solicitado por un único médico.
3. **Se Realiza (Paciente ⇄ Análisis)** → Relación **1:N**
    - Un paciente puede tener múltiples análisis, pero cada análisis pertenece a un solo paciente.

---

### **Transformación al Modelo Relacional**

### **Tablas y Claves**

### 1️⃣ **Tabla Medico**

Represento a los médicos en el sistema.

```sql
CREATE TABLE Medico (
    dni CHAR(10) PRIMARY KEY,
    numColegiado VARCHAR(20) UNIQUE,
    nombre VARCHAR(100)
);
```

- **PK**: `dni` (Identifica de forma única a cada médico)
- **Restricción**: `numColegiado` debe ser único.

---

### 2️⃣ **Tabla Paciente**

Represento a los pacientes atendidos por los médicos.

```sql
CREATE TABLE Paciente (
    dni CHAR(10) PRIMARY KEY,
    numSegSocial VARCHAR(20) UNIQUE,
    nombre VARCHAR(100)
);
```

- **PK**: `dni` (Identifica de forma única a cada paciente)
- **Restricción**: `numSegSocial` debe ser único.

---

### 3️⃣ **Tabla Atiende (Médico ⇄ Paciente, Relación N:M)**

Creo ahora una tabla intermedia para manejar la relación de muchos a muchos.

```sql
CREATE TABLE Atiende (
    dni_medico CHAR(10),
    dni_paciente CHAR(10),
    PRIMARY KEY (dni_medico, dni_paciente),
    FOREIGN KEY (dni_medico) REFERENCES Medico(dni) ON DELETE CASCADE,
    FOREIGN KEY (dni_paciente) REFERENCES Paciente(dni) ON DELETE CASCADE
);
```

- **PK**: `(dni_medico, dni_paciente)` (Cada combinación es única)
- **FK**: `dni_medico` referencia a `Medico.dni`
- **FK**: `dni_paciente` referencia a `Paciente.dni`

---

### 4️⃣ **Tabla Analisis**

Almaceno los análisis clínicos realizados a los pacientes.

```sql
CREATE TABLE Analisis (
    analisisID INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    parametro VARCHAR(100),
    valor VARCHAR(100),
    dni_paciente CHAR(10),
    FOREIGN KEY (dni_paciente) REFERENCES Paciente(dni) ON DELETE CASCADE
);
```

- **PK**: `analisisID` (Cada análisis tiene un identificador único)
- **FK**: `dni_paciente` referencia a `Paciente.dni`

---

### 5️⃣ **Tabla Solicita (Médico ⇄ Análisis, Relación 1:N)**

Recapitulando un poco, sabemos que cada análisis es solicitado por un solo médico, pero un médico puede solicitar varios análisis.

```sql
CREATE TABLE Solicita (
    analisisID INT,
    dni_medico CHAR(10),
    PRIMARY KEY (analisisID, dni_medico),
    FOREIGN KEY (analisisID) REFERENCES Analisis(analisisID) ON DELETE CASCADE,
    FOREIGN KEY (dni_medico) REFERENCES Medico(dni) ON DELETE CASCADE
);
```

- **PK**: `(analisisID, dni_medico)` (Cada solicitud es única)
- **FK**: `analisisID` referencia a `Analisis.analisisID`
- **FK**: `dni_medico` referencia a `Medico.dni`

---

Este modelo relacional cumple con la **Tercera Forma Normal (3FN)** porque:

✔️ **No hay grupos repetitivos** (1FN).

✔️ **Cada atributo depende totalmente de la clave primaria** (2FN).

✔️ **No existen dependencias transitivas** (3FN).

## **Exercise 3: Database Creation in MySQL**

### **Database Creation**

```sql
CREATE DATABASE HOSPITAL;
USE HOSPITAL;
```

---

### **Table Creation**

**Table Doctor**

```sql
CREATE TABLE Doctor (
    dni CHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    licenseNumber VARCHAR(20) UNIQUE NOT NULL
);
```

---

**Table Patient**

```sql
CREATE TABLE Patient (
    dni CHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    socialSecurityNumber VARCHAR(20) UNIQUE NOT NULL
);
```

---

**Table Analysis**

```sql
CREATE TABLE Analysis (
    analysisID INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    parameter VARCHAR(100) NOT NULL,
    value DECIMAL(10,2) NOT NULL,
    patient_dni CHAR(10) NOT NULL,
    FOREIGN KEY (patient_dni) REFERENCES Patient(dni) ON DELETE CASCADE
);
```

---

**Table Medical Attention (N:M Relationship between Doctors and Patients)**

```sql
CREATE TABLE Attends (
    doctor_dni CHAR(10) NOT NULL,
    patient_dni CHAR(10) NOT NULL,
    PRIMARY KEY (doctor_dni, patient_dni),
    FOREIGN KEY (doctor_dni) REFERENCES Doctor(dni) ON DELETE CASCADE,
    FOREIGN KEY (patient_dni) REFERENCES Patient(dni) ON DELETE CASCADE
);
```

---

**Table Requests (1:N Relationship between Doctor and Analysis)**

```sql
CREATE TABLE Requests (
    analysisID INT NOT NULL,
    doctor_dni CHAR(10) NOT NULL,
    PRIMARY KEY (analysisID, doctor_dni),
    FOREIGN KEY (analysisID) REFERENCES Analysis(analysisID) ON DELETE CASCADE,
    FOREIGN KEY (doctor_dni) REFERENCES Doctor(dni) ON DELETE CASCADE
);
```

---

### **Data Insertion**

**Doctors (20 example records)**

```sql
INSERT INTO Doctor (dni, name, licenseNumber) VALUES
('987654321B', 'Dr. Natalia Matarranz', 'MC-54321'),
('123456789A', 'Dr. Juan Pérez', 'MC-40000'),
('234567890C', 'Dr. Luis Martínez', 'MC-49000'),
('345678901D', 'Dr. Ana López', 'MC-50500'),
('456789012E', 'Dr. Carlos Ramírez', 'MC-52000'),
('567890123F', 'Dr. Laura Fernández', 'MC-53010'),
('678901234G', 'Dr. Pablo Torres', 'MC-54230'),
('789012345H', 'Dr. Carmen Ruiz', 'MC-55000'),
('890123456I', 'Dr. Antonio Sánchez', 'MC-56050'),
('901234567J', 'Dr. Beatriz Gómez', 'MC-57025'),
('012345678K', 'Dr. Sergio Díaz', 'MC-58015'),
('112233445L', 'Dr. Rosa Ortega', 'MC-59030'),
('223344556M', 'Dr. Vicente Herrera', 'MC-60020'),
('334455667N', 'Dr. Patricia Moreno', 'MC-61045'),
('445566778O', 'Dr. Manuel Castro', 'MC-62055'),
('556677889P', 'Dr. Natalia Ríos', 'MC-63035'),
('667788990Q', 'Dr. Eduardo Vázquez', 'MC-64010'),
('778899001R', 'Dr. Julia Navarro', 'MC-65060'),
('889900112S', 'Dr. Francisco Delgado', 'MC-66070'),
('990011223T', 'Dr. Elena Suárez', 'MC-67080');
```

---

**Patients (20 example records)**

```sql
INSERT INTO Patient (dni, name, socialSecurityNumber) VALUES
('33333333C', 'Carlos Rodríguez', '4567890123C'),
('44444444D', 'Ana Martínez', '5678901234D'),
('55555555E', 'Pedro Gómez', '6789012345E'),
('66666666F', 'Laura Sánchez', '7890123456F'),
('77777777G', 'María Fernández', '8901234567G'),
('88888888H', 'Javier Pérez', '9012345678H'),
('99999999I', 'Elena Ortega', '0123456789I'),
('11111111J', 'Fernando López', '1234567890J'),
('22222222K', 'Sofía Ramírez', '2345678901K'),
('12121212L', 'Miguel Torres', '3456789012L'),
('23232323M', 'Patricia Díaz', '4567890123M'),
('34343434N', 'Alejandro Navarro', '5678901234N'),
('45454545O', 'Lucía Castro', '6789012345O'),
('56565656P', 'David Herrera', '7890123456P'),
('67676767Q', 'Andrea Vázquez', '8901234567Q'),
('78787878R', 'Ricardo Suárez', '9012345678R'),
('89898989S', 'Natalia Delgado', '0123456789S'),
('90909090T', 'Cristina Moreno', '1234567890T'),
('10101010U', 'Guillermo Ríos', '2345678901U'),
('21212121V', 'Carolina Gómez', '3456789012V');
```

---

**Analyses (20 example records)**

```sql
INSERT INTO Analysis (date, parameter, value, patient_dni) VALUES
('2024-02-01', 'Cholesterol', 190.0, '33333333C'),
('2024-03-10', 'Glucose', 110.5, '44444444D'),
('2023-12-20', 'Cholesterol', 210.0, '55555555E'),
('2023-06-15', 'Triglycerides', 150.0, '66666666F'),
('2024-01-22', 'Glucose', 95.0, '77777777G'),
('2024-03-05', 'Uric Acid', 5.3, '88888888H'),
('2023-09-17', 'Cholesterol', 180.2, '99999999I'),
('2023-11-12', 'Triglycerides', 130.0, '11111111J'),
('2024-02-18', 'Glucose', 102.7, '22222222K'),
('2024-03-21', 'Uric Acid', 6.1, '33333333C'),
('2023-07-30', 'Cholesterol', 200.0, '44444444D'),
('2023-05-05', 'Triglycerides', 140.8, '55555555E'),
('2024-02-08', 'Glucose', 120.0, '66666666F'),
('2023-10-14', 'Uric Acid', 4.8, '77777777G'),
('2023-12-01', 'Cholesterol', 175.5, '88888888H'),
('2024-01-27', 'Triglycerides', 160.0, '99999999I'),
('2023-11-05', 'Glucose', 105.2, '11111111J'),
('2024-03-11', 'Cholesterol', 190.6, '22222222K'),
('2023-08-23', 'Uric Acid', 5.9, '33333333C'),
('2023-06-20', 'Glucose', 98.7, '44444444D');
```

---

**Medical Attention (Relationships between doctors and patients)**

```sql
INSERT INTO Attends (doctor_dni, patient_dni) VALUES
('987654321B', '33333333C'),
('123456789A', '44444444D'),
('234567890C', '55555555E'),
('345678901D', '66666666F'),
('987654321B', '77777777G'),
('123456789A', '88888888H'),
('234567890C', '99999999I'),
('345678901D', '11111111J'),
('987654321B', '22222222K'),
('123456789A', '12121212L'),
('234567890C', '23232323M'),
('345678901D', '34343434N'),
('987654321B', '45454545O'),
('123456789A', '56565656P'),
('234567890C', '67676767Q'),
('345678901D', '78787878R'),
('987654321B', '89898989S'),
('123456789A', '90909090T'),
('234567890C', '10101010U'),
('345678901D', '21212121V');
```

---

**Analysis Requests (Association between doctors and requested analyses)**

```sql
INSERT INTO Requests (analysisID, doctor_dni) VALUES
(1, '987654321B'),
(2, '123456789A'),
(3, '234567890C'),
(4, '345678901D'),
(5, '987654321B'),
(6, '123456789A'),
(7, '234567890C'),
(8, '345678901D'),
(9, '987654321B'),
(10, '123456789A'),
(11, '234567890C'),
(12, '345678901D'),
(13, '987654321B'),
(14, '123456789A'),
(15, '234567890C'),
(16, '345678901D'),
(17, '987654321B'),
(18, '123456789A'),
(19, '234567890C'),
(20, '345678901D');
```

---

### **Requested Queries**

**Query 1: Cholesterol analyses performed by the doctor with DNI '123456789A'**

```sql
SELECT A.*
FROM Analysis A
JOIN Requests R ON A.analysisID = R.analysisID
WHERE R.doctor_dni = '123456789A' AND A.parameter = 'Cholesterol';
```

---

**Query 2: Cholesterol analyses with a value greater than 120**

```sql
SELECT * FROM Analysis
WHERE parameter = 'Cholesterol' AND value > 120;
```

---

**Query 3: Analyses performed after January 1, 2023**

```sql
SELECT * FROM Analysis
WHERE date > '2023-01-01';
```

---

**Query 4: Cholesterol analyses by doctors whose name starts with 'Dr.' and license number < 'MC-50000'**

```sql
SELECT A.*
FROM Analysis A
JOIN Requests R ON A.analysisID = R.analysisID
JOIN Doctor D ON R.doctor_dni = D.dni
WHERE D.name LIKE 'Dr.%' AND D.licenseNumber < 'MC-50000' AND A.parameter = 'Cholesterol';
```

---

**Query 5: Patients, analyses performed, and the name of the doctor who requested them**

```sql
SELECT P.name AS Patient, A.date, A.parameter, A.value, D.name AS Doctor
FROM Patient P
JOIN Analysis A ON P.dni = A.patient_dni
JOIN Requests R ON A.analysisID = R.analysisID
JOIN Doctor D ON R.doctor_dni = D.dni;
```

---

**Query 6: Patients and their analyses (including those without analyses), along with the doctor**

```sql
SELECT P.name AS Patient, A.date, A.parameter, A.value, D.name AS Doctor
FROM Patient P
LEFT JOIN Analysis A ON P.dni = A.patient_dni
LEFT JOIN Requests R ON A.analysisID = R.analysisID
LEFT JOIN Doctor D ON R.doctor_dni = D.dni;
```

---

**Query 7: Patients with at least one glucose analysis**

```sql
SELECT DISTINCT P.name
FROM Patient P
JOIN Analysis A ON P.dni = A.patient_dni
WHERE A.parameter = 'Glucose';
```

---

**Query 8: Number of analyses performed by each doctor**

```sql
SELECT D.name, COUNT(R.analysisID) AS Total_Analyses
FROM Doctor D
LEFT JOIN Requests R ON D.dni = R.doctor_dni
GROUP BY D.name;
```

---

**Query 9: Patients who have not had any analyses**

```sql
SELECT P.name
FROM Patient P
LEFT JOIN Analysis A ON P.dni = A.patient_dni
WHERE A.analysisID IS NULL;
```

---

**Query 10: Patients who have had more than three analyses**

```sql
SELECT P.name
FROM Patient P
JOIN Analysis A ON P.dni = A.patient_dni
GROUP BY P.name
HAVING COUNT(A.analysisID) > 3;
```

## **Exercise 4:** Write the RA expressions to obtain the requested data

### 🔹 A) Customers from Zaragoza who have purchased more than 10 units of a product

1. **Filter customers from Zaragoza**
    
    ```sql
    CustomersZaragoza ← σ_{city='Zaragoza'}(CUSTOMERS)
    ```
    
2. **Filter sales with quantity greater than 10**
    
    ```sql
    SalesGreaterThan10 ← σ_{quantity > 10}(SALES)
    ```
    
3. **Join the filtered tables to get customers from Zaragoza who purchased more than 10 units**
    
    ```sql
    Result ← π_{customer_id, name} (CustomersZaragoza ⨝ SalesGreaterThan10)
    ```
    

---

### 🔹 B) Products priced above €2000 and sold more than 10 times

### **Steps:**

1. **Filter products priced above €2000**
    
    ```sql
    ExpensiveProducts ← σ_{price > 2000}(PRODUCTS)
    ```
    
2. **Group sales by product and calculate the total quantity sold**
    
    ```sql
    SalesByProduct ← γ_{product_id, SUM(quantity) → total_sold}(SALES)
    ```
    
3. **Filter products sold more than 10 times**
    
    ```sql
    SalesGreaterThan10 ← σ_{total_sold > 10}(SalesByProduct)
    ```
    
4. **Join expensive products with the filtered sales**
    
    ```sql
    Result ← π_{product_id, description} (ExpensiveProducts ⨝ SalesGreaterThan10)
    ```
    

---

### 🔹 C) Customers who have purchased exactly 5 distinct products

### **Steps:**

1. **Group sales by customer and count distinct products purchased**
    
    ```sql
    ProductsByCustomer ← γ_{customer_id, COUNT(DISTINCT product_id) → num_products}(SALES)
    ```
    
2. **Filter customers who purchased exactly 5 distinct products**
    
    ```sql
    Customers5Products ← σ_{num_products = 5}(ProductsByCustomer)
    ```
    
3. **Join with the CUSTOMERS table to get their names**
    
    ```sql
    Result ← π_{customer_id, name} (Customers5Products ⨝ CUSTOMERS)
    ```
    

---

### 🔹 D) Product IDs that have not been purchased by more than 5 customers

### **Steps:**

1. **Count the number of distinct customers who purchased each product**
    
    ```sql
    CustomersByProduct ← γ_{product_id, COUNT(DISTINCT customer_id) → num_customers}(SALES)
    ```
    
2. **Filter products not purchased by more than 5 customers**
    
    ```sql
    ProductsNotMoreThan5 ← σ_{num_customers ≤ 5}(CustomersByProduct)
    ```
    
3. **Select only the product IDs**
    
    ```sql
    Result ← π_{product_id} (ProductsNotMoreThan5)
    ```
    

---

### 🔹 E) Products priced the same as the product with the lowest price

### **Steps:**

1. **Get the minimum price of the products**
    
    ```sql
    MinPrice ← γ_{MIN(price) → min_price}(PRODUCTS)
    ```
    
2. **Select products with that price**
    
    ```sql
    ProductsSamePrice ← σ_{price = min_price} (PRODUCTS × MinPrice)
    ```
    
3. **Get the product ID and description**
    
    ```sql
    Result ← π_{product_id, description} (ProductsSamePrice)
    ```
    

---

### 🔹 F) Customers who have purchased products from more than 2 different categories

1. **Join sales with the products table to get the categories**
    
    ```sql
    SalesWithCategories ← SALES ⨝ PRODUCTS
    ```
    
2. **Count distinct categories per customer**
    
    ```sql
    CategoriesByCustomer ← γ_{customer_id, COUNT(DISTINCT category) → num_categories}(SalesWithCategories)
    ```
    
3. **Filter customers with more than 2 different categories**
    
    ```sql
    CustomersMoreThan2 ← σ_{num_categories > 2}(CategoriesByCustomer)
    ```
    
4. **Join with CUSTOMERS to get their names**
    
    ```sql
    Result ← π_{customer_id, name} (CustomersMoreThan2 ⨝ CUSTOMERS)
    ```
    

## 5. References and External Support

Para la resolución de esta práctica ha sido esencial el uso de material externo complementario al temario de la asignatura para garantizar la asimilación de conocimientos sobre el contenido. 

**W3 Schools (SQL)**:

https://www.w3schools.com/sql/default.asp

**geeksforgeeks (mysql):** 

https://www.geeksforgeeks.org/mysql-tutorial/?ref=gcse_outind

**IBM tutorial de bases de datos relacionales y no relacionales:**
https://www.youtube.com/watch?v=E9AgJnsEvG4

https://www.youtube.com/watch?v=OqjJjpjDRLc&pp=ygUUcmVsYXRpb2FibCBkYXRhYmFzZXM%3D

**Codewars (app de retos de programación para aprendizaje):**
https://www.codewars.com/kata/5809508cc47d327c12000084

https://www.codewars.com/kata/65ba1120b51541407b4ed4ce

**Github Personal para contenidos de la universidad:**

https://github.com/ismaelucky342/U-Tad