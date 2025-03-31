-- Creation of the database
CREATE DATABASE ExampleDataTypes;
USE ExampleDataTypes;

-- Table with all data types
CREATE TABLE DataTypes (
    id INT PRIMARY KEY AUTO_INCREMENT,       -- Auto-incremental integer (primary key)
    
    -- 🔢 Numeric Types
    small_integer TINYINT,                   -- Small integer (-128 to 127) or (0 to 255 UNSIGNED)
    medium_integer SMALLINT,                 -- Medium integer (-32,768 to 32,767)
    normal_integer INT,                      -- Standard integer (-2,147,483,648 to 2,147,483,647)
    large_integer BIGINT,                    -- Large integer (-9 quintillion to 9 quintillion)

    small_decimal DECIMAL(5,2),              -- Decimal with 5 total digits and 2 decimals (e.g., 999.99)
    large_decimal NUMERIC(10,4),             -- Decimal with 10 digits and 4 decimals
    floating_point FLOAT,                    -- Floating-point number (lower precision)
    double_precision DOUBLE,                 -- Floating-point number with higher precision
    
    -- 📝 Text and String Types
    fixed_character CHAR(10),                -- Fixed-length string of 10 characters
    variable_character VARCHAR(50),          -- String of up to 50 characters (stores only what is needed)
    long_text TEXT,                          -- Variable-length text up to 65,535 characters

    -- 📆 Date and Time Types
    date DATE,                               -- Date only (YYYY-MM-DD)
    time TIME,                               -- Time only (HH:MI:SS)
    date_time DATETIME,                      -- Date and time (YYYY-MM-DD HH:MI:SS)
    current_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp with the current date
    year_column YEAR,                        -- Year (format YYYY)

    -- 🟢 Booleans (In MySQL, it is a TINYINT(1) with values 1 or 0)
    boolean BOOLEAN,                         -- Boolean (1 = true, 0 = false)

    -- 🖼️ Binary Data (Images, files)
    binary_file BLOB,                        -- Stores large binary files

    -- 🌐 JSON and Unstructured Data
    json_data JSON,                          -- Stores data in JSON format

    -- 🎨 Enumerated and Set Types
    enum_column ENUM('Option1', 'Option2', 'Option3'),  -- Enumeration with predefined values
    set_column SET('Value1', 'Value2', 'Value3')        -- Set with multiple predefined values
);

-- Insertion of example data
INSERT INTO DataTypes (
    small_integer, medium_integer, normal_integer, large_integer, 
    small_decimal, large_decimal, floating_point, double_precision, 
    fixed_character, variable_character, long_text, 
    date, time, date_time, year_column, boolean, binary_file, json_data, 
    enum_column, set_column
) VALUES (
    100, 32000, 2147483647, 9000000000000, 
    99.99, 12345.6789, 3.14, 2.71828, 
    'A', 'Example of VARCHAR', 'This is a long text.', 
    '2024-03-31', '14:30:00', '2024-03-31 14:30:00', 2024, 
    1, NULL, '{"name": "John", "age": 30}', 
    'Option1', 'Value1,Value2'
);

-- Displaying the inserted data
SELECT * FROM DataTypes;
