-- Display records from second_table where name exists
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
