-- drop database mooninsurance;
-- -- Create the database

CREATE DATABASE IF NOT EXISTS mooninsurance;
USE mooninsurance;


-- Drop tables if they exist (clean start)
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS agents;

-- Create agents table
CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_code VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    branch VARCHAR(100),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    product_types TEXT,
    hire_date DATE
);

-- Insert sample agents
INSERT INTO agents (agent_code, first_name, last_name, branch, contact_number, email, product_types, hire_date)
VALUES
('AGT001', 'Nimal', 'Perera', 'Colombo', '0771234567', 'nimal@example.com', 'Life, Health', '2023-04-01'),
('AGT002', 'Saman', 'Silva', 'Kandy', '0772345678', 'saman@example.com', 'Life, Vehicle', '2022-06-15'),
('AGT003', 'Ruwan', 'Fernando', 'Matara', '0773456789', 'ruwan@example.com', 'Health', '2024-01-10');

-- Create sales table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_code VARCHAR(50) NOT NULL,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    sale_date DATE,
    branch VARCHAR(100),
    FOREIGN KEY (agent_code) REFERENCES agents(agent_code) ON DELETE CASCADE
);

-- Insert sample sales
INSERT INTO sales (agent_code, product_name, amount, sale_date, branch)
VALUES
('AGT001', 'Life Insurance - Premium Plan', 150000.00, '2024-03-10', 'Colombo'),
('AGT002', 'Vehicle Insurance - Full Coverage', 85000.00, '2024-03-12', 'Kandy'),
('AGT003', 'Health Insurance - Family', 120000.00, '2024-03-15', 'Matara');

-- Create notifications table
CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agent_code VARCHAR(50),
    message TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_code) REFERENCES agents(agent_code) ON DELETE SET NULL
);

-- Insert sample notifications
INSERT INTO notifications (agent_code, message)
VALUES
('AGT001', '🎉 Nimal has reached 150k sales milestone!'),
('AGT002', '🎯 Reminder: Vehicle sales target due this week.'),
('AGT003', '🚀 Ruwan’s monthly health insurance target achieved!');

-- SET SQL_SAFE_UPDATES = 0;

-- DELETE FROM notifications;
-- DELETE FROM sales;
-- DELETE FROM agents;

-- SET SQL_SAFE_UPDATES = 1;

SELECT * FROM notifications;
SELECT * FROM sales;
SELECT * FROM agents;

ALTER TABLE agents
DROP COLUMN product_types,
ADD COLUMN team ENUM('Alpha', 'Beta', 'Gamma', 'Delta') DEFAULT 'Alpha';

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(100) NOT NULL,
    product_name VARCHAR(150) NOT NULL,
    target_amount DECIMAL(10,2) NOT NULL
);

ALTER TABLE sales
DROP COLUMN product_name,
ADD COLUMN product_id INT,
ADD CONSTRAINT fk_product_id
    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
    ON DELETE SET NULL;


INSERT INTO agents (agent_code, first_name, last_name, branch, contact_number, email, team, hire_date)
VALUES
('AGT001', 'Nimal', 'Perera', 'Colombo', '0771234567', 'nimal@example.com', 'Team A', '2023-04-01'),
('AGT002', 'Saman', 'Silva', 'Kandy', '0772345678', 'saman@example.com', 'Team B', '2022-06-15'),
('AGT003', 'Ruwan', 'Fernando', 'Matara', '0773456789', 'ruwan@example.com', 'Team A', '2024-01-10'),
('AGT004', 'Ishara', 'Jayasinghe', 'Galle', '0774567890', 'ishara@example.com', 'Team C', '2023-07-20'),
('AGT005', 'Kavindu', 'De Silva', 'Negombo', '0775678901', 'kavindu@example.com', 'Team B', '2023-10-05');




