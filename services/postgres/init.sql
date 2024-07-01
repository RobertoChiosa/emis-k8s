-- Create table for meters
CREATE TABLE meter
(
    id          INTEGER PRIMARY KEY,
    description TEXT,
    type_id     INTEGER,
    quantity_id INTEGER,
    unit_id     INTEGER,
    FOREIGN KEY (type_id) REFERENCES monitoring_class (id),
    FOREIGN KEY (quantity_id) REFERENCES monitoring_quantity (id),
    FOREIGN KEY (unit_id) REFERENCES monitoring_unit (id)
);

-- Create table for monitoring units
CREATE TABLE unit
(
    id         INTEGER PRIMARY KEY,
    name       TEXT,
    symbol     TEXT,
    definition TEXT,
    iri        TEXT
);

-- Create table for monitoring quantities
CREATE TABLE quantity
(
    id         INTEGER PRIMARY KEY,
    name       TEXT,
    definition TEXT,
    iri        TEXT
);

-- Create table for monitoring classes
CREATE TABLE class
(
    id         INTEGER PRIMARY KEY,
    name       TEXT,
    definition TEXT,
    iri        TEXT
);

-- Populate the meter table
COPY meter
    FROM '/docker-entrypoint-initdb.d/meter.csv'
    DELIMITER ','
    CSV HEADER;

-- Populate the monitoring_unit table
COPY unit
    FROM '/docker-entrypoint-initdb.d/unit.csv'
    DELIMITER ','
    CSV HEADER;

-- Populate the monitoring_quantity table
COPY quantity
    FROM '/docker-entrypoint-initdb.d/quantity.csv'
    DELIMITER ','
    CSV HEADER;

-- Populate the monitoring_class table
COPY class
    FROM '/docker-entrypoint-initdb.d/class.csv'
    DELIMITER ','
    CSV HEADER;
