#!/usr/bin/mysql
-- create a User
-- create a Database
-- Give the user all the necessary permissions

CREATE USER IF NOT EXISTS 'user_blog'@'localhost' IDENTIFIED BY 'passwd';
CREATE DATABASE IF NOT EXISTS db_blog;
GRANT ALL PRIVILEGES ON db_blog.* TO 'user_blog'@'localhost';
FLUSH PRIVILEGES;