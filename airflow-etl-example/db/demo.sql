-- source_students table
SELECT * FROM source_students ORDER by id LIMIT 10;

SELECT COUNT(*) FROM source_students;

-- target_students table
SELECT * FROM target_students ORDER by id LIMIT 10;

SELECT COUNT(*) FROM target_students;

-- join `source_students` with `target_students`
SELECT s.id, s.first_name as source_first_name, t.first_name as target_first_name, s.last_name as source_last_name, t.last_name as target_last_name
FROM source_students as s
INNER JOIN target_students as t
ON s.id=t.id
ORDER by id
LIMIT 10;
