CREATE TABLE sensors
(
    id   TEXT,
    name TEXT
);

COPY sensors
    FROM '/docker-entrypoint-initdb.d/sensors.csv'
    DELIMITER ','
    CSV HEADER;