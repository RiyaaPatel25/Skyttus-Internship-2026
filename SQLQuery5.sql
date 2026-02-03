CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(30),
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(40) NOT NULL
);

