-- UPDATE students
-- SET birth_date = '1998-11-02'
-- WHERE last_name = 'Benichou';

-- UPDATE students
-- SET last_name = 'Guez'
-- WHERE first_name = 'David';

-- DELETE FROM students
-- WHERE first_name = 'Lea' AND last_name = 'Benichou';

-- SELECT count(*)
-- FROM students;

-- SELECT count(*)
-- FROM students
-- WHERE birth_date > '01-01-2000';

-- ALTER TABLE students ADD math_grade smallint;

-- UPDATE students
-- SET math_grade = 80
-- WHERE id = 1;
--
-- UPDATE students
-- SET math_grade = 90
-- WHERE id IN (2,4);
--
-- UPDATE students
-- SET math_grade = 40
-- WHERE id = 6;
--
-- SELECT count(*)
-- FROM students
-- WHERE math_grade > 83;

-- INSERT INTO students (first_name, last_name, birth_date, math_grade)
-- VALUES ('Omer', 'Simpson', '1980-10-03', 70);

-- SELECT sum(math_grade) AS sum_math_grades FROM students;


