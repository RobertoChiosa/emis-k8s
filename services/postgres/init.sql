-- Create table for meters
-- Create table for  units
CREATE TABLE unit
(
    id   INTEGER PRIMARY KEY,
    name TEXT,
    iri  TEXT
);

-- Create table for  quantities
CREATE TABLE quantity
(
    id   INTEGER PRIMARY KEY,
    name TEXT,
    iri  TEXT
);

-- Create table for  classes
CREATE TABLE class
(
    id   INTEGER PRIMARY KEY,
    name TEXT,
    iri  TEXT
);

CREATE TABLE meter
(
    id          INTEGER PRIMARY KEY,
    description TEXT,
    type_id     INTEGER,
    quantity_id INTEGER,
    unit_id     INTEGER,
    FOREIGN KEY (type_id) REFERENCES class (id),
    FOREIGN KEY (quantity_id) REFERENCES quantity (id),
    FOREIGN KEY (unit_id) REFERENCES unit (id)
);

-- Populate the _unit table
COPY unit
    FROM '/docker-entrypoint-initdb.d/unit.csv'
    DELIMITER ','
    CSV HEADER;

-- Populate the _quantity table
COPY quantity
    FROM '/docker-entrypoint-initdb.d/quantity.csv'
    DELIMITER ','
    CSV HEADER;

-- Populate the _class table
COPY class
    FROM '/docker-entrypoint-initdb.d/class.csv'
    DELIMITER ','
    CSV HEADER;

-- Populate the meter table
COPY meter
    FROM '/docker-entrypoint-initdb.d/meter.csv'
    DELIMITER ','
    CSV HEADER;