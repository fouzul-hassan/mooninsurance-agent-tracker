-- Create the database
CREATE DATABASE IF NOT EXISTS mooninsurance;
USE moon_insurance;

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
