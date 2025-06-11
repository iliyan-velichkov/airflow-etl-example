-- source_employees table
SELECT * FROM source_employees ORDER by id LIMIT 10;

SELECT COUNT(*) FROM source_employees;

-- target_employees table
SELECT * FROM target_employees ORDER by id LIMIT 10;

SELECT COUNT(*) FROM target_employees;

-- join `source_employees` with `target_employees`
SELECT s.id, s.first_name as SOURCE_first_name, t.first_name as TARGET_first_name, s.last_name as SOURCE_last_name, t.last_name as TARGET_last_name
FROM source_employees as s
INNER JOIN target_employees as t
ON s.id=t.id
ORDER by id
LIMIT 10;
