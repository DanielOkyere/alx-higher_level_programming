-- creates database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
