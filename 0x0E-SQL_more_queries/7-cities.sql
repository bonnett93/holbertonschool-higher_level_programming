-- Creates the database hbtn_0d_usa and the table cities.
-- State_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL);
