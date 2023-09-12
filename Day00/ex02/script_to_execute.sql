CREATE TABLE data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct FROM '/tmp/data_2022_oct.csv' CSV HEADER;