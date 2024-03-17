-- create table students
--         (
-- id SERIAL PRIMARY KEY,
-- last_name VARCHAR (100) NOT NULL,
-- first_name VARCHAR (50) NOT NULL,
-- birth_date DATE NOT NULL
--         );

-- insert into students(last_name, first_name, birth_date)
-- values ('Benichou','Marc','11/02/1998'), ('Cohen','Yoan','12/03/2010'), ('Benichou','Lea','07/27/1987'), ('Dux','Amelia','04/07/1996'), ('Grez','David','06/14/2003'), ('Simpson','Omer','10/03/1980');

-- insert into students(last_name, first_name, birth_date)
-- values ('Arkhipov','Gregory','10/16/1996');

-- SELECT * from students;
--
-- SELECT first_name, last_name from students;

-- SELECT first_name, last_name from students WHERE id=2;

-- SELECT first_name, last_name from students WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- SELECT first_name, last_name from students WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- SELECT first_name, last_name from students WHERE first_name ILIKE'%a%';

-- SELECT first_name, last_name from students WHERE first_name ILIKE'A%';

-- SELECT first_name, last_name from students WHERE first_name ILIKE'%a';

-- SELECT first_name, last_name from students WHERE first_name ILIKE'_%a%';

-- SELECT first_name, last_name from students WHERE first_name ILIKE'%a';

-- SELECT first_name, last_name from students WHERE id = 1 or id = 3;

-- SELECT id, first_name, last_name, birth_date from students WHERE birth_date >= '01/01/2000';

-- SELECT first_name, last_name, birth_date from students ORDER BY last_name ASC LIMIT 4;

-- SELECT first_name, last_name, birth_date from students ORDER BY birth_date DESC LIMIT 1;

-- SELECT first_name, last_name, birth_date from students OFFSET 2  LIMIT 3;

