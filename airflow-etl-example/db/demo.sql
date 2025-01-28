-- Source table
CREATE TABLE source_students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

INSERT INTO source_students(first_name, last_name)
VALUES 
    ('John', 'Doe'),
    ('Jane', 'Smith');

SELECT * FROM source_students;

-- Destination table
CREATE TABLE target_students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

SELECT * FROM target_students;
