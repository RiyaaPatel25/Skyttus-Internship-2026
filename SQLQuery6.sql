CREATE TABLE account (
	account_id INT,
	name VARCHAR(50),
	balance INT
);

--start a transaction
BEGIN TRANSACTION;

--insert reccord into account
INSERT INTO account(account_id,name,balance) VALUES
(111,'Riya',5000),
(112,'Maitri',6000),
(113,'Brij',4000);

--rollback changes
ROLLBACK;

--demonstrate transfer of money using transaction
--sender
UPDATE account
SET balance = balance - 500
WHERE account_id = 112;

--receiver
UPDATE account 
SET balance = balance + 500
WHERE account_id = 113;

--commit valid transactions
COMMIT;

SELECT * FROM account;


