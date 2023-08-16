-- lists all records of second_name table. Skip rows with no name
SELECT score, name
FROM second_table
WHERE score IS NOT NULL;
