-- Create a subquery that lists all the cities of Califonia
SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = 'Califonia')
ORDER BY id;
