-- script that creates the table unique_id on your MySQL server.
-- I would use a unique key when you have columns you know shouldn’t contain duplicates.

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
