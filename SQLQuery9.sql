CREATE TABLE emplyee (
	id INT PRIMARY KEY,
	name VARCHAR(50),
	salary INT,
	hiredate DATE
);

INSERT INTO emplyee VALUES
(1,'Riya',50000,'2025-10-08'),
(2,'Tiya',60000,'2025-11-15'),
(4,'Riha',50000,'2025-01-12'),
(5,'Rita',60000,'2024-11-09');

--Find Nth(2nd) highest salary
SELECT salary
FROM (
	SELECT salary,
		DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
		FROM emplyee
	)temp
WHERE rnk = 2;

--remove duplicate records
CREATE TABLE persons(
	id INT,
	name VARCHAR(50),
	city VARCHAR(50)
);

INSERT INTO persons VALUES
(1,'Riya','Chikhali'),
(2,'Maitri','Surat'),
(2,'Maitri','Surat'),
(3,'Jainee','Navsari'),
(3,'Jainee','Navsari');

WITH CTE AS (
	SELECT *,
		ROW_NUMBER() OVER (
			PARTITION BY id,name,city 
			ORDER BY id
			) As rn
	FROM persons
)
DELETE FROM CTE WHERE rn>1;

SELECT * FROM persons;

--Find records common in two tables
CREATE TABLE table1 (
	id INT,
	name VARCHAR(50)
);

CREATE TABLE table2 (
	id INT,
	name VARCHAR(50)
);

INSERT INTO table1 VALUES
(1,'Riya'),
(2,'Maitri'),
(3,'Brij');

INSERT INTO table2 VALUES
(2,'Maitri'),
(3,'Brij'),
(4,'Rahi');

SELECT a.*
FROM table1 a
INNER JOIN table2 b
	ON a.id = b.id AND a.name = b.name;

--Find employees hired in last 6 months
SELECT *
FROM emplyee
WHERE hiredate >= DATEADD(MONTH, -6,GETDATE());

--Find continuous duplicate values
CREATE TABLE logs (
	id INT,
	value INT
);

INSERT INTO logs VALUES
(1,10),
(2,20),
(3,20),
(4,30),
(5,40),
(6,40);

SELECT DISTINCT value
FROM (
	SELECT value,
		LAG(value) OVER (ORDER BY id) AS prevalue
	FROM logs
	)t
WHERE value = prevalue;

SELECT value,
		LAG(value) OVER (ORDER BY id) AS prevalue
	FROM logs;


