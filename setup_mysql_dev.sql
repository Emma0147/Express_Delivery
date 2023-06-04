-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS expressdelivery;
CREATE USER IF NOT EXISTS 'ed_dev'@'localhost' IDENTIFIED BY 'ed_dev_pwd';
GRANT ALL PRIVILEGES ON `expressdelivery`.* TO 'ed_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ed_dev'@'localhost';
FLUSH PRIVILEGES;
