-- Example 1: Candidate Key and Primary Key
CREATE TABLE Students (
    StudentID INT PRIMARY KEY, -- Primary Key
    Email VARCHAR(255) UNIQUE -- Candidate Key
);

-- Example 2: Alternative Key
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY, -- Primary Key
    NationalID VARCHAR(20) UNIQUE -- Alternative Key
);

-- Example 3: Foreign Key
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Example 4: Composite Primary Key
CREATE TABLE Enrollment (
    StudentID INT,
    CourseID INT,
    PRIMARY KEY (StudentID, CourseID) -- Composite Primary Key
);

-- Example 5: Multiple Candidate Keys
CREATE TABLE Products (
    ProductID INT PRIMARY KEY, -- Primary Key
    SKU VARCHAR(50) UNIQUE, -- Candidate Key
    Barcode VARCHAR(50) UNIQUE -- Candidate Key
);

-- Example 6: Foreign Key with ON DELETE CASCADE
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    OrderID INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Example 7: Foreign Key with ON UPDATE CASCADE
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY,
    OrderID INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON UPDATE CASCADE
);

-- Example 8: Self-referencing Foreign Key
CREATE TABLE EmployeesHierarchy (
    EmployeeID INT PRIMARY KEY,
    ManagerID INT,
    FOREIGN KEY (ManagerID) REFERENCES EmployeesHierarchy(EmployeeID)
);

-- Example 9: Unique Constraint as Candidate Key
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentCode VARCHAR(10) UNIQUE -- Candidate Key
);

-- Example 10: Foreign Key with Composite Key
CREATE TABLE CourseAssignments (
    InstructorID INT,
    CourseID INT,
    PRIMARY KEY (InstructorID, CourseID), -- Composite Primary Key
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);