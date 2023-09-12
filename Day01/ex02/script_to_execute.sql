DELETE FROM customers
WHERE ctid NOT IN (
    SELECT DISTINCT ON (event_time, event_type, product_id, price, user_id, user_session) ctid
    FROM customers
);
