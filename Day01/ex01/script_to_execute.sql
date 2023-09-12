
CREATE TABLE IF NOT EXISTS customers (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);
INSERT INTO customers (event_time, event_type, product_id, price, user_id, user_session)
(
    SELECT event_time, event_type, product_id, price, user_id, user_session FROM data_2022_oct
    UNION ALL
    SELECT event_time, event_type, product_id, price, user_id, user_session FROM data_2022_nov
    UNION ALL
    SELECT event_time, event_type, product_id, price, user_id, user_session FROM data_2022_dec
    UNION ALL
    SELECT event_time, event_type, product_id, price, user_id, user_session FROM data_2023_feb
    UNION ALL
    SELECT event_time, event_type, product_id, price, user_id, user_session FROM data_2023_jan
    UNION ALL
);