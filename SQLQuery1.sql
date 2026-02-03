CREATE TABLE students(
      student_id INT,
      name VARCHAR(50),
      department VARCHAR(30),
      year INT,
      marks INT
);

INSERT INTO students VALUES 
(1, 'Riya', 'IT', 4, 85),
(2, 'Maitri', 'CSE', 2, 90),
(3, 'Krisha', 'IT', 3, 94),
(4, 'Jainee', 'EC', 2, 93),
(5, 'Dhruvi', 'CSE', 1, 74);

--Display all records
SELECT * FROM students;

--Display only name and department
SELECT name,department FROM students;

--Display students with marks greater than 75
SELECT * FROM students
WHERE marks > 75 ;

--Display students from CSE department
SELECT * FROM students
WHERE department = 'CSE';

--Display students by marks (Descending)
SELECT * FROM students
ORDER BY marks DESC;

--Display top 3 scorer
SELECT TOP 3 * FROM students
ORDER BY marks DESC











