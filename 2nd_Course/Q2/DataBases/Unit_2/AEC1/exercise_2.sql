-- ============================================================
-- **Exercise 2: Transformation of the E-R Model**
-- ============================================================

-- **Entities and Attributes**
-- From the provided E-R diagram, we identify the following entities:

-- 1. **Medico** (Doctor)
-- Attributes: dni, numColegiado, nombre
-- 2. **Paciente** (Patient)
-- Attributes: dni, numSegSocial, nombre
-- 3. **Analisis** (Analysis)
-- Attributes: analisisID, fecha, parametro, valor

-- **Relationships and Cardinalities**
-- The diagram shows three important relationships:

-- 1. **Atiende (Medico ⇄ Paciente)** → Relationship **N:M**
--    - A doctor can attend to many patients, and a patient can be attended by many doctors.
--    - A table is created to manage this relationship.
-- 2. **Solicita (Medico ⇄ Analisis)** → Relationship **1:N**
--    - A doctor can request many analyses, but each analysis is requested by only one doctor.
-- 3. **Se Realiza (Paciente ⇄ Analisis)** → Relationship **1:N**
--    - A patient can have many analyses, but each analysis belongs to only one patient.

-- ============================================================
-- **Relational Model Transformation**
-- ============================================================

-- 1️⃣ **Table Medico** (Doctor)
-- This table represents the doctors in the system.
CREATE TABLE Medico (
    dni CHAR(10) PRIMARY KEY,
    numColegiado VARCHAR(20) UNIQUE,
    nombre VARCHAR(100)
);

-- 2️⃣ **Table Paciente** (Patient)
-- This table represents the patients attended by the doctors.
CREATE TABLE Paciente (
    dni CHAR(10) PRIMARY KEY,
    numSegSocial VARCHAR(20) UNIQUE,
    nombre VARCHAR(100)
);

-- 3️⃣ **Table Atiende** (Medico ⇄ Paciente, Relationship N:M)
-- Creating an intermediate table to manage the many-to-many relationship.
CREATE TABLE Atiende (
    dni_medico CHAR(10),
    dni_paciente CHAR(10),
    PRIMARY KEY (dni_medico, dni_paciente),
    FOREIGN KEY (dni_medico) REFERENCES Medico(dni) ON DELETE CASCADE,
    FOREIGN KEY (dni_paciente) REFERENCES Paciente(dni) ON DELETE CASCADE
);

-- 4️⃣ **Table Analisis** (Analysis)
-- Storing clinical analysis performed on patients.
CREATE TABLE Analisis (
    analisisID INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    parametro VARCHAR(100),
    valor VARCHAR(100),
    dni_paciente CHAR(10),
    FOREIGN KEY (dni_paciente) REFERENCES Paciente(dni) ON DELETE CASCADE
);

-- 5️⃣ **Table Solicita** (Medico ⇄ Analisis, Relationship 1:N)
-- Storing which doctor requested each analysis.
CREATE TABLE Solicita (
    analisisID INT,
    dni_medico CHAR(10),
    PRIMARY KEY (analisisID, dni_medico),
    FOREIGN KEY (analisisID) REFERENCES Analisis(analisisID) ON DELETE CASCADE,
    FOREIGN KEY (dni_medico) REFERENCES Medico(dni) ON DELETE CASCADE
);

-- ============================================================
-- **Explanation of the Relational Model:**
-- In this relational model:
-- - We have separate tables for Medico, Paciente, and Analisis.
-- - The relationship between Medico and Paciente is managed with an intermediate table called "Atiende".
-- - The relationship between Medico and Analisis is handled using the "Solicita" table.
-- - The relationship between Paciente and Analisis is naturally handled in the "Analisis" table with a foreign key reference to Paciente.

-- This model is in **Third Normal Form (3NF)** because:
-- ✅️ **No repeating groups** (1NF).
-- ✅️ **All attributes depend fully on the primary key** (2NF).
-- ✅️ **No transitive dependencies** (3NF).
