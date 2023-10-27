-- Searches for all cities of california
SELECT id, name 
FROM cities
WHERE id = (
	SELECT id FROM states WHERE name = 'Carlifonia'
)
ORDER BY id ASC;
