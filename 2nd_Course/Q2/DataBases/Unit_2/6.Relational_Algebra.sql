-- Let's assume a relational model with the following tables:
-- Students(id_student, name, age, id_course)
-- Courses(id_course, course_name, professor)

-- Example 1: Selection (σ)
-- Get students older than 20 years.
SELECT * 
FROM Students 
WHERE age > 20;

-- In relational algebra:
-- σ_age>20(Students)

-- Example 2: Projection (π)
-- Get the names and ages of the students.
SELECT name, age 
FROM Students;

-- In relational algebra:

-- π_name,age(Students)

-- Example 3: Union (∪)
-- Get a combined list of student names and course names.
SELECT name 
FROM Students
UNION
SELECT course_name 
FROM Courses;


-- In relational algebra:
-- π_name(Students) ∪ π_course_name(Courses)

-- Example 4: Cartesian Product (×)
-- Combine students with courses.
SELECT * 
FROM Students, Courses;

-- In relational algebra:
-- Students × Courses

-- Example 5: Join (⨝)
-- Get students with the name of their course.
SELECT Students.name, Courses.course_name 
FROM Students
JOIN Courses 
ON Students.id_course = Courses.id_course;

-- In relational algebra:
-- Students ⨝_Students.id_course=Courses.id_course Courses

-- Example 6: Difference (-)
-- Get students who are not enrolled in any course.
SELECT * 
FROM Students
WHERE id_course NOT IN (SELECT id_course FROM Courses);

-- In relational algebra:
-- Students - π_id_student(Students ⨝ Courses)

-- Example 7: Intersection (∩)
-- Get students who are also professors (assuming a professor table with names).
SELECT name 
FROM Students
INTERSECT
SELECT name 
FROM Professors;

-- In relational algebra:
-- π_name(Students) ∩ π_name(Professors)

-- Example 8: Division (÷)
-- Get students enrolled in all courses taught by a specific professor.
-- Assuming a table Professors(id_professor, name, id_course).
SELECT id_student 
FROM Enrollments
GROUP BY id_student
HAVING COUNT(DISTINCT id_course) = (SELECT COUNT(*) FROM Courses WHERE professor = 'John Doe');

-- In relational algebra:
-- π_id_student(Enrollments) ÷ π_id_course(σ_professor='John Doe'(Courses))

-- Example 9: Aggregation (γ)
-- Get the average age of students.
SELECT AVG(age) AS average_age 
FROM Students;

-- In relational algebra:
-- γ_avg(age)(Students)

-- Example 10: Rename (ρ)
-- Rename the Students table to Learners.
-- In SQL, this is typically done using aliases.
SELECT * 
FROM Students AS Learners;

-- In relational algebra:
-- ρ_Learners(Students)