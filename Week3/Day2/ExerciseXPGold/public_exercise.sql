-- CREATE TABLE purchases (
--     id SERIAL PRIMARY KEY,
--     customer_id INTEGER REFERENCES customers(id),
--     item_id INTEGER REFERENCES items(id),
--     quantity_purchased INTEGER
-- );
--
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
--     (SELECT id FROM items WHERE item_name = 'Fan'),
--     1
-- );
--
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
--     (SELECT id FROM items WHERE item_name = 'Large desk'),
--     10
-- );
--
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (
--     (SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
--     (SELECT id FROM items WHERE item_name = 'Small Desk'),
--     2
-- );

-- SELECT *
-- FROM purchases;

-- SELECT c.first_name, c.last_name, p.quantity_purchased
-- FROM purchases AS p
-- JOIN customers AS c ON p.customer_id = c.id;

-- SELECT *
-- FROM purchases
-- WHERE customer_id = 5

-- SELECT *
-- FROM purchases
-- WHERE item_id IN (1,2)

-- SELECT c.first_name, c.last_name, i.item_name
-- FROM purchases AS p
-- JOIN customers AS c  ON p.customer_id = c.id
-- JOIN public.items AS i on i.id = p.item_id;

-- INSERT INTO purchases (customer_id, quantity_purchased) VALUES (1, 5); -- Added new row with null in item_id column because there is no NOT NULL constrain