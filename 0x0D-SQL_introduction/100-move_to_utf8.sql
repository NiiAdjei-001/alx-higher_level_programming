-- convert hbtn_0c_0 database to UTF8 
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0
ALTER TABLE first_table
DEFAULT CHARSET=utf8mb4,
MODIFY COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
