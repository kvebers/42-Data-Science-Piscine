CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT DEFAULT 0,
    user_id BIGINT DEFAULT -1,
    user_session UUID DEFAULT '00000000-0000-0000-0000-000000000000'
);

COPY data_2022_oct FROM '/tmp/data_2022_oct.csv' CSV HEADER;

CREATE TABLE IF NOT EXISTS data_2022_nov (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT DEFAULT 0,
    user_id BIGINT DEFAULT -1,
    user_session UUID DEFAULT '00000000-0000-0000-0000-000000000000'
);

COPY data_2022_nov FROM '/tmp/data_2022_nov.csv' CSV HEADER;

CREATE TABLE IF NOT EXISTS data_2022_dec (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT DEFAULT 0,
    user_id BIGINT DEFAULT -1,
    user_session UUID DEFAULT '00000000-0000-0000-0000-000000000000'
);

COPY data_2022_dec FROM '/tmp/data_2022_dec.csv' CSV HEADER;



CREATE TABLE IF NOT EXISTS data_2023_jan (
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_type VARCHAR(255) DEFAULT 'unknown_event',
    product_id INT DEFAULT -1,
    price FLOAT DEFAULT -1.0,
    user_id BIGINT DEFAULT -1,
    user_session UUID DEFAULT '00000000-0000-0000-0000-000000000000'
);

COPY data_2023_jan FROM '/tmp/data_2023_jan.csv' CSV HEADER;

CREATE TABLE IF NOT EXISTS data_2023_feb (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT DEFAULT 0,
    user_id BIGINT DEFAULT -1,
    user_session UUID DEFAULT '00000000-0000-0000-0000-000000000000'
);

COPY data_2023_feb FROM '/tmp/data_2023_feb.csv' CSV HEADER;