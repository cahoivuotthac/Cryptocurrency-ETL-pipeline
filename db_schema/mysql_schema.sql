CREATE DATABASE IF NOT EXISTS Cryptocurrency_Marketplace;

DROP TABLE IF EXISTS Cryptocurrency_Info;
CREATE TABLE Cryptocurrency_Marketplace.Cryptocurrency_Info (
    id INT PRIMARY KEY,
    crypto_name VARCHAR(100) UNIQUE,          
    crypto_slug VARCHAR(100) UNIQUE,          
    crypto_symbol VARCHAR(10),
    crypto_logo_url VARCHAR(255)           
);

DROP TABLE IF EXISTS Cryptocurrency_Metrics;
CREATE TABLE Cryptocurrency_Marketplace.Cryptocurrency_Metrics (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    crypto_id INT,
    cmc_rank INT,                      
    num_market_pairs INT,               
    circulating_supply INT,             
    last_updated DATETIME, 
    FOREIGN KEY (crypto_id) REFERENCES Cryptocurrency_Info(id)
);

DROP TABLE IF EXISTS Cryptocurrency_USD_Quote;
CREATE TABLE Cryptocurrency_Marketplace.Cryptocurrency_USD_Quote (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    crypto_id INT,
    usd_current_price DECIMAL(36, 18),
    usd_volume_24h DECIMAL(36, 18),
    usd_volume_percent_change_24h DECIMAL(36, 18),
    usd_price_percent_change_1h DECIMAL(36, 18),
    usd_price_percent_change_24h DECIMAL(36, 18),
    usd_price_percent_change_7d DECIMAL(36, 18),
    usd_price_percent_change_30d DECIMAL(36, 18),
    usd_market_cap DECIMAL(36, 18),
    usd_market_cap_dominance DECIMAL(36, 18),   
    last_updated DATETIME,
    FOREIGN KEY (crypto_id) REFERENCES Cryptocurrency_Info(id)
);

DROP TABLE IF EXISTS Global_Market;
CREATE TABLE Cryptocurrency_Marketplace.Global_Market (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    active_cryptocurrencies INT,
    total_cryptocurrencies INT,
    active_market_pairs INT,
    active_exchanges INT,              
    total_exchanges INT,
    usd_total_market_cap DECIMAL(36, 18),
    usd_total_volume_24h DECIMAL(36, 18),
    usd_total_market_cap_yesterday DECIMAL(36, 18),
    usd_total_volume_24h_yesterday DECIMAL(36, 18),
    usd_total_market_cap_yesterday_percentage_change DECIMAL(36, 18),
    usd_total_volume_24h_yesterday_percentage_change DECIMAL(36, 18),
    last_updated DATETIME
);

DROP TABLE IF EXISTS Global_Market_Dominances;
CREATE TABLE Cryptocurrency_Marketplace.Global_Market_Dominances (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    global_market_id BIGINT,
    crypto_id INT,             
    dominance_percentage DECIMAL(36, 18),       
    dominance_percentage_yesterday DECIMAL(36, 18),
    dominance_percentage_change_24h DECIMAL(36, 18),
    last_updated DATETIME,
    FOREIGN KEY (global_market_id) REFERENCES Global_Market(id),
    FOREIGN KEY (crypto_id) REFERENCES Cryptocurrency_Info(id)
);
