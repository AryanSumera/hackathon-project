CREATE DATABASE coreinventory;

-- PRODUCTS TABLE
-- stores product information

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(100) UNIQUE NOT NULL,
    unit VARCHAR(20),
    per_unit_cost NUMERIC(10,2)
);



-- WAREHOUSES TABLE
-- where products are stored

CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);



-- INVENTORY TABLE
-- tracks stock levels

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),

    on_hand INT DEFAULT 0,
    free_to_use INT DEFAULT 0
);



-- RECEIPTS TABLE
-- stock coming into warehouse

CREATE TABLE receipts (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),

    quantity INT NOT NULL,
    per_unit_cost NUMERIC(10,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- DELIVERIES TABLE
-- stock leaving warehouse

CREATE TABLE deliveries (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),

    quantity INT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- STOCK MOVES TABLE
-- movement between warehouses

CREATE TABLE moves (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),

    source_warehouse INT REFERENCES warehouses(id),
    destination_warehouse INT REFERENCES warehouses(id),

    quantity INT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

