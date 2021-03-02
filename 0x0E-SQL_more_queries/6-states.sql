-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
-- id INT unique, auto generated, cant be null and is a primary key
-- name VARCHAR(256) cant be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- if the table states already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE, name VARCHAR(256) NOT NULL);