-- Creates database hbtn_0d_usa and the table states
-- id i unique, not null, auto generated and a pk
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (id)
);
