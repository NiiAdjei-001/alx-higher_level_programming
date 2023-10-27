-- Searches for all cities within the state  of california
SELECT cities.id, cities.name 
FROM cities
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California')
ORDER BY cities.id ASC;
