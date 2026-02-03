CREATE DATABASE company_db

CREATE TABLE department(
	dept_id INT PRIMARY KEY,
	dept_name VARCHAR(50)
);

CREATE TABLE employees(
	emp_id INT PRIMARY KEY,
	emp_name VARCHAR(50),
	dept_id INT,
	salary INT,
	FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

INSERT INTO department VALUES
(1,'HR'),
(2,'Finance'),
(3,'IT');

INSERT INTO employees VALUES
(101, 'Riya', 3, 45000),
(102, 'Maitri', 2, 55000),
(103, 'Jainee', 1, 65000),
(104, 'Dhruvi', 3, 40000),
(105, 'Amit', 3, 70000),
(106, 'Diya', NULL, 35000);

--Display employee name with department name
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN department d
ON d.dept_id = e.dept_id;

--Display employee earning more than 50000
SELECT emp_name, salary
FROM employees
WHERE salary > 50000;

--Display department-wise total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN department d
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

--Display department with more than 2 employees
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count 
FROM employees e
INNER JOIN department d
ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;

--Display employees without department
SELECT emp_name
FROM employees e
LEFT JOIN department d
ON d.dept_id = e.dept_id
WHERE d.dept_id IS NUll;






















