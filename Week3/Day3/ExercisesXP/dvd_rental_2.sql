-- UPDATE film SET language_id = 2 WHERE film_id = 1;
-- UPDATE film SET language_id = 2 WHERE film_id = 2;
-- UPDATE film SET language_id = 2 WHERE film_id = 3;

-- store_id and address_id are foreign keys for the customer table. You need to pass this keys when INSERT something into the customer table

-- drop table customer_review
-- it will drop easily because it's a child table

-- SELECT COUNT(*)
-- FROM (SELECT film.title
--       FROM film
--       LEFT JOIN inventory
--       ON film.film_id = inventory.film_id
--       WHERE inventory.film_id IS NULL);

-- SELECT film.film_id, film.title, film.rental_rate
-- FROM film
-- LEFT JOIN inventory
-- ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL
-- ORDER BY rental_rate DESC, title ASC
-- FETCH FIRST 30 ROWS ONLY

-- SELECT film.title
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor a on a.actor_id = film_actor.actor_id
-- WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe' AND film.description ILIKE '%sumo wrestler%'

-- SELECT title
-- FROM film
-- WHERE length <= 60 AND rating = 'R' AND description ILIKE '%documentary%'

-- SELECT title
-- FROM film
-- JOIN inventory ON film.film_id = inventory.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND film.rental_rate > 4.00
-- AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- SELECT title, replacement_cost
-- FROM film
-- JOIN inventory ON film.film_id = inventory.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND (film.description ILIKE '%boat%' OR film.title ILIKE '%boat%')
-- ORDER BY replacement_cost DESC
-- LIMIT 1


