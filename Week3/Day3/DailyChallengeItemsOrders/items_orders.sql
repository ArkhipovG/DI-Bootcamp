-- CREATE TABLE product_orders (
--     order_id SERIAL PRIMARY KEY,
--     customer_id INTEGER,
--     order_date DATE
-- );
--
-- CREATE TABLE items (
--     item_id SERIAL PRIMARY KEY,
--     order_id INTEGER,
--     product_name VARCHAR(255),
--     price DECIMAL(10, 2),
--     FOREIGN KEY (order_id) REFERENCES product_orders(order_id)
-- );


-- INSERT INTO product_orders (customer_id, order_date)
-- VALUES (1, '2024-03-19');
--
-- INSERT INTO items (order_id, product_name, price)
-- VALUES (1, 'Stone Fire', 10.99),
--        (1, 'Money Harold', 20.49);

-- CREATE OR REPLACE FUNCTION calculate_order_total(order_id_param INTEGER)
-- RETURNS DECIMAL AS $$
-- DECLARE
--     total DECIMAL := 0;
-- BEGIN
--     SELECT SUM(price) INTO total
--     FROM items
--     WHERE order_id = order_id_param;
--
--     RETURN total;
-- END;
-- $$ LANGUAGE plpgsql;
--
-- select calculate_order_total(1)