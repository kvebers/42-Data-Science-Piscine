CREATE TEMPORARY TABLE temp AS SELECT DISTINCT * FROM customers;
TRUNCATE customers;
INSERT INTO customers SELECT * FROM temp;
