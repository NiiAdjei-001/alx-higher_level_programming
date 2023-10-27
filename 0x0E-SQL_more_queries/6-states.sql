-- Create database hbtn_0d_usa.
-- Create table states in hbtn_0d_usa.
-- States attributes (id, name)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
