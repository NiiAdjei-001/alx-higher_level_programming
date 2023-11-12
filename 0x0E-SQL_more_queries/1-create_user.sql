-- Creates a user 'user_0d_1@localhost' with pass 'user_0d_1_pwd'
-- Grant user privileges and permissions
--  Privileges :: ALL PRIVILEGES, CREATE, DROP, DELETE, INSERT, SELECT, UPDATE
--  Permissions :: <DATABASE_NAME>.<TABLE_NAME>
-- Flush privileges to refresh
CREATE USER [IF NOT EXISTS] 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES 
ON *.* 
TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
