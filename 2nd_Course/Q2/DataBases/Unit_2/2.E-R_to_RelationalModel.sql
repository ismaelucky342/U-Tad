-- Example of transforming an E-R model to a relational model

-- Simple entities
CREATE TABLE Student (
    Student_ID INT PRIMARY KEY,
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Birth_Date DATE
);

CREATE TABLE Course (
    Course_ID INT PRIMARY KEY,
    Course_Name VARCHAR(100),
    Credits INT
);

-- One-to-many relationship (1:N)
-- A student can be enrolled in multiple courses
CREATE TABLE Enrollment (
    Enrollment_ID INT PRIMARY KEY,
    Student_ID INT,
    Course_ID INT,
    Enrollment_Date DATE,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);

-- Many-to-many relationship (N:M)
-- Professors can teach multiple courses, and a course can be taught by multiple professors
CREATE TABLE Professor (
    Professor_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Specialty VARCHAR(100)
);

CREATE TABLE Teaches (
    Professor_ID INT,
    Course_ID INT,
    PRIMARY KEY (Professor_ID, Course_ID),
    FOREIGN KEY (Professor_ID) REFERENCES Professor(Professor_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);

-- One-to-one relationship (1:1)
-- Each student has a unique ID card
CREATE TABLE ID_Card (
    ID_Card_ID INT PRIMARY KEY,
    Student_ID INT UNIQUE,
    Issue_Date DATE,
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
);