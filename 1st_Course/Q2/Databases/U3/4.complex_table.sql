CREATE TABLE Students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthdate DATE,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    course_id INT,
    PRIMARY KEY (student_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE SET NULL,
    CHECK (phone_number LIKE '+%')
);
