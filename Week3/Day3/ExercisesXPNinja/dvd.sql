-- SELECT f.title, f.rating, rental_date, rental_id
-- FROM film f
-- LEFT JOIN inventory i ON f.film_id = i.film_id
-- LEFT JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE f.rating IN ('G', 'PG')
-- AND (r.rental_id IS NULL OR r.return_date IS NOT NULL);

-- CREATE TABLE waiting_list (
--     waiting_id SERIAL PRIMARY KEY,
--     customer_id INTEGER REFERENCES customer(customer_id),
--     film_id INTEGER REFERENCES film(film_id),
--     rental_id INTEGER REFERENCES rental(rental_id)
-- );

-- INSERT INTO waiting_list (customer_id, film_id) VALUES
-- (1, 101),
-- (2, 101),
-- (3, 102),
-- (4, 101),
-- (5, 103);
--
-- SELECT w.film_id, COUNT(*) AS waiting_count
-- FROM waiting_list w
-- GROUP BY w.film_id;

