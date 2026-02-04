--Add index to improve search on orders.cutomer_id
CREATE NONCLUSTERED INDEX idx_orders_customer_id
ON orderss(customer_id);

SELECT *
FROM orderss
WHERE customer_id = 1;

--Use EXPLAIN to analyze query
SET STATISTICS PROFILE ON;

SELECT c.name, o.amount
FROM customers c
JOIN orderss o 
	ON c.customer_id = o.customer_id

SET STATISTICS PROFILE OFF;

--Optimize a slow join query
SELECT c.name, o.amount
FROM customers c
JOIN orderss o 
	ON c.customer_id = o.customer_id;

--When index should not be used

-- Index should not be used when:
-- 1. A large percentage of rows are returned
-- 2. Column has very low cardinality
-- 3. Full table scan is faster than index lookup
-- Example:
-- WHERE order_date BETWEEN '2025-02-01' AND '2025-01-28'

-- Example query where index may not be useful
SELECT *
FROM orderss
WHERE order_date BETWEEN '2025-02-01' AND '2025-01-28';