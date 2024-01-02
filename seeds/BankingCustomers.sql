DROP TABLE IF EXISTS customers;
DROP SEQUENCE IF EXISTS customers_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;
CREATE SEQUENCE IF NOT EXISTS customers_id_seq;
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    contactnumber VARCHAR(20)
);
CREATE SEQUENCE IF NOT EXISTS Accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    accountname TEXT,
    accountnumber INTEGER,
    accountbalance NUMERIC(1000),
    customerid INTEGER
);

INSERT INTO customers (FirstName, LastName, ContactNumber) VALUES ('Leah', 'Southern', '+447732443654');
INSERT INTO customers (FirstName, LastName, ContactNumber) VALUES ('John', 'Doe', '+447932445396');
INSERT INTO customers (FirstName, LastName, ContactNumber) VALUES ('Alan', 'Carr', '+447921124786');

INSERT INTO accounts (AccountName, AccountNumber, AccountBalance, CustomerID) VALUES ('Premier', 2009223,  3000, 1);
INSERT INTO accounts (AccountName, AccountNumber, AccountBalance, CustomerID) VALUES ('Savings', 3009004, 5000, 2);
INSERT INTO accounts (AccountName, AccountNumber, AccountBalance, CustomerID) VALUES ('Black', 4332367, 10000, 3);
INSERT INTO accounts (AccountName, AccountNumber, AccountBalance, CustomerID) VALUES ('Ruby', 2076554, 11245, 1);