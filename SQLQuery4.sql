--Find Employees earning more than average salary
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

--Find Department with highest total salary
SELECT TOP 1 d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN department d
ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC

--Display Employee with second highest salary
SELECT TOP 1 emp_name , salary
FROM (
	SELECT TOP 2 emp_name,salary
	FROM employees
	ORDER BY salary DESC
	) AS temp
ORDER BY salary ASC;

--Display employees working on same department "Amit"
SELECT emp_name , dept_id
FROM employees
WHERE dept_id = (
	SELECT dept_id
	FROM employees
	WHERE emp_name = 'Amit'
);




