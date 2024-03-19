-- SELECT name
-- from language;

-- SELECT film.title, film.description, language.name
-- from film
-- JOIN language ON film.language_id = language.language_id;

-- SELECT film.title, film.description, language.name
-- from language
-- LEFT JOIN film ON film.language_id = language.language_id

-- create table new_film(
-- id SERIAL PRIMARY KEY,
-- name VARCHAR (255) NOT NULL
-- );
--
-- INSERT INTO new_film (name)
-- VALUES ('Snatch'), ('Gentlemen'), ('Lock, Stock and Two Smoking Barrels');

-- create table customer_review(
-- review_id SERIAL PRIMARY KEY,
-- film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
-- language_id INTEGER REFERENCES language(language_id),
-- title VARCHAR (255) NOT NULL,
-- score INTEGER CHECK (score >= 1 AND score <= 10),
-- review_text TEXT,
-- last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
--
-- INSERT  INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (1, 1, 'Amazing scenario', 10, 'This movie is perfect in all its categories: credits, sound track, production, casting, writing, photography, editing, acting, and direction');
--
-- INSERT  INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (2, 1, 'Goldfingers', 9, 'At first I thought it started a little slowly but in hindsight it was just right. A perfect execution of a classic British gangster film epitomised by a charismatic Colin Farrell who stole every scene he entered and left me crying out for a coach spin off. All in all very enjoyable classic guy ritchie film');

-- DELETE FROM new_film
-- WHERE id = 2; -- in customer_review the row also deleted
