-- create table items
--         (
--         );
-- create table customers
--         (
--         );
-- alter table customers
--             add id serial primary key;
-- alter table customers
--             add first_name varchar(50) not null;
-- alter table customers
--             add last_name varchar(100) not null;
-- alter table items
--             add id serial primary key;
-- alter table items
--             add item_name varchar(100) not null;
-- alter table items
--             add price integer not null;
--
-- INSERT INTO public.customers (id, first_name, last_name) VALUES (1, 'Greg', 'Jones');
-- INSERT INTO public.customers (id, first_name, last_name) VALUES (2, 'Sandra', 'Jones');
-- INSERT INTO public.customers (id, first_name, last_name) VALUES (3, 'Scott', 'Scott');
-- INSERT INTO public.customers (id, first_name, last_name) VALUES (4, 'Trevor', 'Green');
-- INSERT INTO public.customers (id, first_name, last_name) VALUES (5, 'Melanie', 'Johnson');
--
-- INSERT INTO public.items (id, item_name, price) VALUES (1, 'Small Desk', 100);
-- INSERT INTO public.items (id, item_name, price) VALUES (2, 'Large desk', 300);
-- INSERT INTO public.items (id, item_name, price) VALUES (3, 'Fan', 80);
--
-- SELECT * FROM items;
--
-- SELECT * FROM items WHERE price > 80;
--
-- SELECT * FROM items WHERE price <= 300;
--
-- SELECT * FROM customers WHERE last_name = 'Smith'; -- It shows nobody
--
-- SELECT * FROM customers WHERE last_name = 'Jones';
--
-- SELECT * FROM customers WHERE first_name != 'Scott';
--
--