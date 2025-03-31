-- Example of DML exercise

-- Create a table for students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE,
    Major VARCHAR(50)
);

-- Create a table for courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Credits INT
);

-- Create a table for enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    Grade DECIMAL(3, 2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Insert data into Students table
INSERT INTO Students (StudentID, FirstName, LastName, BirthDate, Major)
VALUES
(1, 'Alice', 'Johnson', '2000-05-15', 'Computer Science'),
(2, 'Bob', 'Smith', '1999-08-22', 'Mathematics'),
(3, 'Charlie', 'Brown', '2001-03-10', 'Physics'),
(4, 'Diana', 'White', '2000-11-30', 'Biology');

-- Insert data into Courses table
INSERT INTO Courses (CourseID, CourseName, Credits)
VALUES
(101, 'Database Systems', 4),
(102, 'Calculus II', 3),
(103, 'Physics I', 4),
(104, 'Biology Basics', 3);

-- Insert data into Enrollments table
INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate, Grade)
VALUES
(1, 1, 101, '2023-01-15', 3.5),
(2, 2, 102, '2023-01-16', 3.8),
(3, 3, 103, '2023-01-17', 3.2),
(4, 4, 104, '2023-01-18', 3.9),
(5, 1, 102, '2023-01-19', 3.7),
(6, 2, 101, '2023-01-20', 3.6);

-- Update a student's major
UPDATE Students
SET Major = 'Data Science'
WHERE StudentID = 1;

-- Update a course's credits
UPDATE Courses
SET Credits = 5
WHERE CourseID = 101;

-- Delete an enrollment record
DELETE FROM Enrollments
WHERE EnrollmentID = 6;

-- Query to find students enrolled in 'Database Systems'
SELECT s.FirstName, s.LastName, c.CourseName, e.Grade
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID
WHERE c.CourseName = 'Database Systems';

-- Query to calculate the average grade for each course
SELECT c.CourseName, AVG(e.Grade) AS AverageGrade
FROM Courses c
JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;

-- Query to list all students and their total credits
SELECT s.FirstName, s.LastName, SUM(c.Credits) AS TotalCredits
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID
GROUP BY s.FirstName, s.LastName;