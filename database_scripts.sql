-- Create the database
CREATE DATABASE IF NOT EXISTS mooninsurance;
USE mooninsurance;

-- Create the agents table
CREATE TABLE IF NOT EXISTS agents (
    agent_code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    permitted_products TEXT
);

-- Insert sample agents
INSERT INTO agents (agent_code, name, branch, email, phone, permitted_products) VALUES
('A001', 'Fouzul Hassan', 'Colombo', 'fouzul@mooninsurance.lk', '0711234567', 'Life, Health'),
('A002', 'Jane Perera', 'Kandy', 'jane.perera@mooninsurance.lk', '0712345678', 'Life'),
('A003', 'Ravi De Silva', 'Galle', 'ravi.desilva@mooninsurance.lk', '0713456789', 'Health, Travel'),
('A004', 'Nimal Fernando', 'Jaffna', 'nimal.fernando@mooninsurance.lk', '0714567890', 'Travel'),
('A005', 'Amaya Gunasekara', 'Kurunegala', 'amaya.gunasekara@mooninsurance.lk', '0715678901', 'Life, Education');

-- Create the sales table
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_code VARCHAR(10),
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    sale_date DATE,
    FOREIGN KEY (agent_code) REFERENCES agents(agent_code)
);

-- Insert sample sales
INSERT INTO sales (agent_code, product_name, amount, sale_date) VALUES
('A001', 'Life', 10000.00, '2025-04-01'),
('A002', 'Life', 7500.50, '2025-04-02'),
('A003', 'Health', 5600.75, '2025-04-03'),
('A001', 'Health', 4200.00, '2025-04-04'),
('A004', 'Travel', 9000.00, '2025-04-04');

-- Create the notifications_sent table
CREATE TABLE IF NOT EXISTS notifications_sent (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agent_code VARCHAR(10),
    message TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_code) REFERENCES agents(agent_code)
);

-- Insert sample notifications
INSERT INTO notifications_sent (agent_code, message) VALUES
('A001', 'Congratulations! You reached your April sales target.'),
('A002', 'Good job! You have achieved your weekly goal.'),
('A003', 'Reminder: You are close to reaching your monthly target.');

-- Create optional aggregated_metrics table
CREATE TABLE IF NOT EXISTS aggregated_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    metric_name VARCHAR(100),
    metric_value VARCHAR(255),
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample metrics
INSERT INTO aggregated_metrics (metric_name, metric_value) VALUES
('Best Performing Branch', 'Colombo'),
('Top Selling Product', 'Life Insurance'),
('Top Agent by Sales', 'Fouzul Hassan');
