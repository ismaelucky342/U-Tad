SELECT s.first_name, s.last_name, COUNT(e.course_id) AS enrolled_courses, AVG(c.duration) AS avg_course_duration
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
GROUP BY s.student_id
HAVING enrolled_courses > 2;
