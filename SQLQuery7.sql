CREATE DATABASE Ecommerce;

CREATE TABLE customers (
	customer_id INT PRIMARY KEY,
	name VARCHAR(100),
	city VARCHAR(100)
);

CREATE TABLE productss (
	product_id INT PRIMARY KEY,
	product_name VARCHAR(100),
	price DECIMAL(10,2)
);

CREATE TABLE orderss (
	order_id INT PRIMARY KEY,
	customer_id INT,
	order_date DATE,
	amount DECIMAL(10,2),
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
	order_id INT,
	product_id INT,
	quantity INT,
	FOREIGN KEY (order_id) REFERENCES orderss(order_id),
	FOREIGN KEY (product_id) REFERENCES productss(product_id)
);

INSERT INTO customers VALUES 
(1,'Riya','Navsari'),
(2,'Priya','Surat'),
(3,'Rita','Valsad'),
(4,'Tiya','Navsari'),
(5,'Diya','Bilimora');

INSERT INTO productss VALUES
(101,'Laptop',40000),
(102,'Keyboard',2000),
(103,'Headphone',8000),
(104,'Mouse',1500),
(105,'Mobile',15000);

INSERT INTO orderss VALUES
(111,1,'2026-01-26',48000),
(112,2,'2026-01-27',3000),
(113,4,'2026-01-29',56000),
(114,5,'2026-02-02',31000),
(115,1,'2026-02-03',42000);

INSERT INTO order_items VALUES
(111,101,1),
(111,103,1),
(112,104,2),
(113,101,1),
(113,103,2),
(114,103,2),
(114,105,1),
(115,101,1),
(115,102,1);

--Total orders per customer
SELECT 
	c.customer_id,
	c.name, 
	COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orderss o
	ON c.customer_id = o.customer_id
GROUP BY c.customer_id,c.name;

--Customer who never placed an order
SELECT 
	c.customer_id,
	c.name 
FROM customers c
LEFT JOIN orderss o 
	ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

--Highest selling product
SELECT TOP 1 
	p.product_id,
	p.product_name,
	SUM(oi.quantity) AS total_quantity
FROM productss p
LEFT JOIN order_items oi
	ON p.product_id = oi.product_id 
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC;

--Monthly sales report
SELECT 
	YEAR(order_date) AS order_year,
	MONTH(order_date) AS order_month,
	SUM(amount) AS total_sales
FROM orderss 
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY order_year,order_month;

--customer with total purchase > 50000
SELECT 
	c.customer_id,
	c.name,
	SUM(o.amount) AS total_purchase
FROM customers c
LEFT JOIN orderss o
	ON c.customer_id = o.customer_id
GROUP BY c.customer_id,c.name
HAVING SUM(amount) > 50000;

--Top 3 cities by revenue
SELECT TOP 3
	c.city,
	SUM(o.amount) AS total_revenue
FROM customers c
LEFT JOIN orderss o
	ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;





