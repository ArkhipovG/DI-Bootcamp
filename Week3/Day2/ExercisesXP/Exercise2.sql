-- select * from customer;

-- select (first_name, last_name) AS full_name from customer

-- select distinct create_date from customer

-- select * from customer order by first_name desc

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate

-- SELECT address.address, address.phone
-- FROM address
-- INNER JOIN customer
-- ON address.address_id = customer.address_id
-- WHERE address.district = 'Texas';

-- select * from film where film_id in (15,150)

-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'Snatch';

-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title LIKE 'Sn%';

-- select *
-- from film
-- order by rental_rate, title
-- fetch first 10 rows only

-- select *
-- from film
-- order by rental_rate, title
-- offset 10
-- fetch next 10 rows only

-- SELECT c.first_name, c.last_name, p.amount, p.payment_date
-- FROM customer AS c
-- JOIN payment AS p ON c.customer_id = p.customer_id
-- ORDER BY c.customer_id;

-- SELECT film.film_id, film.title
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;

-- SELECT city.city, country.country
-- FROM city
-- JOIN country ON city.country_id = country.country_id

-- SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
-- FROM customer AS c
-- JOIN payment AS p ON c.customer_id = p.customer_id
-- ORDER BY p.staff_id








