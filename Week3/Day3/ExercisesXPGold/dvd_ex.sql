-- SELECT rental.rental_id, rental.rental_date, rental.return_date,
--        film.title AS film_title, film.rental_duration
-- FROM rental
-- JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- JOIN film ON inventory.film_id = film.film_id
-- WHERE rental.return_date IS NULL;


-- SELECT rental.rental_id, rental.rental_date,
--        film.title, film.rental_duration, DATE_PART('day', rental.last_update - rental_date) AS days_from_rent
-- FROM rental
-- JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- JOIN film ON inventory.film_id = film.film_id
-- WHERE DATE_PART('day', rental.last_update - rental_date) > film.rental_duration AND return_date IS NULL;
--
-- SELECT (c.first_name, c.last_name) AS full_name
-- FROM rental
-- JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- JOIN film ON inventory.film_id = film.film_id
-- JOIN public.customer c on c.customer_id = rental.customer_id
-- WHERE return_date IS NULL
-- GROUP BY full_name;

-- SELECT film.title, description
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor a on a.actor_id = film_actor.actor_id
-- WHERE a.first_name = 'Joe' AND a.last_name = 'Swank' AND film.description ILIKE '%Action%';


