-- ============================================================
-- **Exercise 3: Transformation of the E-R Model**
-- ============================================================

-- ============================================================
-- **Database Creation**
-- ============================================================

CREATE DATABASE HOSPITAL;
USE HOSPITAL;

---

-- ============================================================
-- **Table Creation**
-- ============================================================

-- 1️⃣ **Table Doctor**
-- This table represents the doctors in the hospital.
CREATE TABLE Doctor (
    dni CHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    licenseNumber VARCHAR(20) UNIQUE NOT NULL
);

---

-- 2️⃣ **Table Patient**
-- This table represents the patients in the hospital.
CREATE TABLE Patient (
    dni CHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    socialSecurityNumber VARCHAR(20) UNIQUE NOT NULL
);

---

-- 3️⃣ **Table Analysis**
-- This table stores clinical analyses performed on patients.
CREATE TABLE Analysis (
    analysisID INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    parameter VARCHAR(100) NOT NULL,
    value DECIMAL(10,2) NOT NULL,
    patient_dni CHAR(10) NOT NULL,
    FOREIGN KEY (patient_dni) REFERENCES Patient(dni) ON DELETE CASCADE
);

---

-- 4️⃣ **Table Medical Attention (N:M Relationship between Doctors and Patients)**
-- This table manages the many-to-many relationship between doctors and patients.
CREATE TABLE Attends (
    doctor_dni CHAR(10) NOT NULL,
    patient_dni CHAR(10) NOT NULL,
    PRIMARY KEY (doctor_dni, patient_dni),
    FOREIGN KEY (doctor_dni) REFERENCES Doctor(dni) ON DELETE CASCADE,
    FOREIGN KEY (patient_dni) REFERENCES Patient(dni) ON DELETE CASCADE
);

---

-- 5️⃣ **Table Requests (1:N Relationship between Doctor and Analysis)**
-- This table stores which doctor requested each analysis.
CREATE TABLE Requests (
    analysisID INT NOT NULL,
    doctor_dni CHAR(10) NOT NULL,
    PRIMARY KEY (analysisID, doctor_dni),
    FOREIGN KEY (analysisID) REFERENCES Analysis(analysisID) ON DELETE CASCADE,
    FOREIGN KEY (doctor_dni) REFERENCES Doctor(dni) ON DELETE CASCADE
);

---

-- ============================================================
-- **Data Insertion**
-- ============================================================

-- 1️⃣ **Doctors (20 example records)**
-- Inserting sample data for doctors.
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

---

-- 2️⃣ **Patients (20 example records)**
-- Inserting sample data for patients.
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

---

-- 3️⃣ **Analyses (20 example records)**
-- Inserting sample data for analyses performed on patients.
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

---

-- 4️⃣ **Medical Attention (Relationships between doctors and patients)**
-- Inserting sample data for the many-to-many relationship between doctors and patients.
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

---

-- 5️⃣ **Analysis Requests (Association between doctors and requested analyses)**
-- Inserting sample data for the one-to-many relationship between doctors and analyses.
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

---

-- ============================================================
-- **Sample Queries**
-- ============================================================

-- 1️⃣ **All doctors with their respective patients**
SELECT d.name AS doctor_name, p.name AS patient_name
FROM Doctor d
JOIN Attends a ON d.dni = a.doctor_dni
JOIN Patient p ON a.patient_dni = p.dni;

-- 2️⃣ **List of patients with their analysis results**
SELECT p.name AS patient_name, a.parameter, a.value, a.date
FROM Patient p
JOIN Analysis a ON p.dni = a.patient_dni;

-- 3️⃣ **Doctors who requested an analysis**
SELECT d.name AS doctor_name, an.parameter AS analysis, r.analysisID
FROM Doctor d
JOIN Requests r ON d.dni = r.doctor_dni
JOIN Analysis an ON r.analysisID = an.analysisID;
