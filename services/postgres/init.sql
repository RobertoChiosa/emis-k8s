-- Create table
CREATE TABLE data
(
    time  TIMESTAMPTZ      NOT NULL,
    value DOUBLE PRECISION NULL,
    uuid  VARCHAR
);

-- Add timescale extension
CREATE extension if not exists timescaledb;

-- Create hypertable to manage timeseries data
SELECT create_hypertable('data', 'time',
                         if_not_exists => TRUE,
                         migrate_data => TRUE,
                         create_default_indexes => TRUE,
                         chunk_time_interval => interval '1 day');

-- Create materialized view for continuous aggregate
CREATE MATERIALIZED VIEW data_1h
    WITH (timescaledb.continuous) AS
SELECT time_bucket('1 h', time) AS bucket,
       uuid,
       avg(value)               AS avg_value
FROM data srt
GROUP BY bucket, uuid;

-- Populate the meter table
COPY data
    FROM '/docker-entrypoint-initdb.d/import/data.csv'
    DELIMITER ','
    CSV HEADER;