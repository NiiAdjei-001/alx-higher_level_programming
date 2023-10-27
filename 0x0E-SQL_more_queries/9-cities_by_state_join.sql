-- Get all cities contained in a database with their respective states
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
