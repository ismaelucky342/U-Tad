-- Example of BCNF (Boyce-Codd Normal Form)
-- Ensuring every determinant is a candidate key
CREATE TABLE Customers_BCNF (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    CustomerAddress VARCHAR(255)
);

CREATE TABLE Products_BCNF (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders_BCNF (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers_BCNF(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products_BCNF(ProductID)
);

-- Example of 4NF (Eliminating Multivalued Dependencies)
CREATE TABLE Customers_4NF (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    CustomerAddress VARCHAR(255)
);

CREATE TABLE Products_4NF (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders_4NF (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers_4NF(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products_4NF(ProductID)
);

-- Example of 5NF (Eliminating Join Dependencies)
CREATE TABLE Customers_5NF (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    CustomerAddress VARCHAR(255)
);

CREATE TABLE Products_5NF (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders_5NF (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers_5NF(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products_5NF(ProductID)
);

-- Example of 6NF (Decomposing to irreducible relations)
-- This is rarely used in practice but shown here for completeness.
CREATE TABLE Customers_6NF (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    CustomerAddress VARCHAR(255)
);

CREATE TABLE Products_6NF (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders_6NF (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers_6NF(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products_6NF(ProductID)
);