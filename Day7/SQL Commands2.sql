select * from customers;


DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

DELETE FROM Customers WHERE CustomerName='Cardinal';

select * from customers;

show tables;

create table temp_customers as (select * from customers);

select * from temp_customers;

update customers 
set age=21;

update temp_customers 
set age=21;

select * from temp_customers;
delete from temp_customers;



CREATE TABLE employee (
    empid INT PRIMARY KEY,
    empname VARCHAR(50),
    deptid INT,
    empsalary DECIMAL(10, 2),
    empage INT
);


INSERT ALL
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (1, 'John Doe', 101, 50000.00, 25)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (2, 'Jane Smith', 102, 55000.00, 30)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (3, 'Robert Johnson', 103, 60000.00, 35)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (4, 'Michael Brown', 104, 65000.00, 40)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (5, 'William Davis', 105, 70000.00, 45)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (6, 'Mary Jones', 101, 75000.00, 50)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (7, 'Patricia Garcia', 102, 80000.00, 28)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (8, 'Linda Martinez', 103, 85000.00, 32)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (9, 'Barbara Wilson', 104, 90000.00, 37)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (10, 'Elizabeth Anderson', 105, 95000.00, 42)
SELECT * FROM dual;

CREATE TABLE department (
    deptid INT PRIMARY KEY,
    deptname VARCHAR(50),
    deptcode VARCHAR(10),
    deptloc VARCHAR(50)
);

select * from employee;

INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;

select * from department;

--cartesian join for the two tables
select * from employee,department;


INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;


-- Create employee table
CREATE TABLE employee (
    empid INT PRIMARY KEY,
    empname VARCHAR(50),
    deptid INT,
    empsalary DECIMAL(10, 2),
    empage INT
);

-- Insert records into employee table
INSERT ALL
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (1, 'John Doe', 101, 50000.00, 25)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (2, 'Jane Smith', 102, 55000.00, 30)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (3, 'Robert Johnson', 103, 60000.00, 35)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (4, 'Michael Brown', 104, 65000.00, 40)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (5, 'William Davis', 105, 70000.00, 45)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (6, 'Mary Jones', 101, 75000.00, 50)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (7, 'Patricia Garcia', 102, 80000.00, 28)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (8, 'Linda Martinez', 103, 85000.00, 32)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (9, 'Barbara Wilson', 104, 90000.00, 37)
INTO employee (empid, empname, deptid, empsalary, empage) VALUES (10, 'Elizabeth Anderson', 105, 95000.00, 42)
SELECT * FROM dual;

-- Create department table
CREATE TABLE department (
    deptid INT PRIMARY KEY,
    deptname VARCHAR(50),
    deptcode VARCHAR(10),
    deptloc VARCHAR(50)
);

-- Insert records into department table
INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;


select * from customers;

select * from employee;

select * from department;

INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT ALL 
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(1, 'Chais', 1, 1, '10 boxes x 20 bags', 18.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(6, 'Grandma''s Boysenberry Spread', 3, 2, '12 - 8 oz jars', 25.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(7, 'Uncle Bob''s Organic Dried Pears', 3, 7, '12 - 1 lb pkgs.', 30.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(8, 'Northwoods Cranberry Sauce', 3, 2, '12 - 12 oz jars', 40.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97.00)
SELECT * FROM DUAL;

select * from products;

SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;


select * from customers;

select * from employee;

select * from department;

INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT ALL 
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(1, 'Chais', 1, 1, '10 boxes x 20 bags', 18.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(6, 'Grandma''s Boysenberry Spread', 3, 2, '12 - 8 oz jars', 25.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(7, 'Uncle Bob''s Organic Dried Pears', 3, 7, '12 - 1 lb pkgs.', 30.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(8, 'Northwoods Cranberry Sauce', 3, 2, '12 - 12 oz jars', 40.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97.00)
SELECT * FROM DUAL;

select * from products;

select CATEGORYID from products;

select COUNT(DISTINCT(CATEGORYID)) from products;


SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;


SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT COUNT(*)
FROM Products;

SELECT COUNT(ProductName)
FROM Products;

SELECT COUNT(DISTINCT(ProductName))
FROM Products;

SELECT COUNT(DISTINCT Price)
FROM Products;

SELECT COUNT(ProductID)
FROM Products
WHERE Price > 20;


SELECT COUNT(*) AS "Number of records"
FROM Products;

SELECT COUNT(*) AS "Number of records",CategoryID
FROM Products
Group By CategoryId
order by Count(*) ASC;


CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);

INSERT ALL  
INTO OrderDetails VALUES (1, 10248, 11, 12)
INTO OrderDetails VALUES (2, 10248, 42, 10)
INTO OrderDetails VALUES (3, 10248, 72, 5)
INTO OrderDetails VALUES (4, 10249, 14, 9)
INTO OrderDetails VALUES (5, 10249, 51, 40)
INTO OrderDetails VALUES (6, 10250, 41, 10)
INTO OrderDetails VALUES (7, 10250, 51, 35)
SELECT * FROM DUAL;


SELECT SUM(Quantity)
FROM OrderDetails;

SELECT SUM(Quantity)
FROM OrderDetails
WHERE ProductId = 11;

SELECT SUM(Quantity) AS total
FROM OrderDetails;

SELECT OrderID, SUM(Quantity) AS "Total Quantity"
FROM OrderDetails
GROUP BY OrderID;

SELECT SUM(Quantity * 10)
FROM OrderDetails;

SELECT SUM(Price * Quantity) AS BILL
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID != Products.ProductID;

SELECT SUM(Price * Quantity) AS BILL
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;

SELECT AVG(Price)
FROM Products;

SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;

SELECT AVG(Price) as "AVG PRICE"
FROM Products
WHERE CategoryID = 1;


SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);


SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;

SELECT * FROM Customers
WHERE CustomerName LIKE 'A%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%A%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%a%';

SELECT Country FROM Customers
WHERE Country LIKE 'C%a';

SELECT country FROM Customers
WHERE country LIKE '%l%';


SELECT country FROM Customers
WHERE country LIKE 'Ca%';

SELECT CustomerName FROM Customers
WHERE CustomerName LIKE 'A%' OR CustomerName LIKE 'B%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'A__%';


--8 characters and above starts with A
SELECT * FROM Customers
WHERE CustomerName LIKE 'A________%';

SELECT * FROM Customers
WHERE Country LIKE 'Canada';

select * from customers;

SELECT * FROM Customers
WHERE CustomerName LIKE '[A-Z]%';

SELECT * FROM Customers
WHERE Country IN ('California', 'Canada', 'UK');


SELECT * FROM Customers
WHERE Country NOT IN ('California', 'Canada', 'UK');

select * from OrderDetails;

SELECT * FROM CUSTOMERS;

SELECT * FROM Customers,OrderDetails
WHERE CustomerID IN (SELECT CustomerID FROM OrderDetails);

SELECT Distinct(Customername) FROM Customers,OrderDetails
WHERE CustomerID IN (SELECT CustomerID FROM OrderDetails);

SELECT * FROM Customers,OrderDetails
WHERE CustomerID NOT IN (SELECT CustomerID FROM OrderDetails);

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID IN (1,2,3);

SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;


-------------------------------------------------------------
select * from customers;

select * from employee;

select * from department;

INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT ALL 
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(1, 'Chais', 1, 1, '10 boxes x 20 bags', 18.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(6, 'Grandma''s Boysenberry Spread', 3, 2, '12 - 8 oz jars', 25.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(7, 'Uncle Bob''s Organic Dried Pears', 3, 7, '12 - 1 lb pkgs.', 30.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(8, 'Northwoods Cranberry Sauce', 3, 2, '12 - 12 oz jars', 40.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97.00)
SELECT * FROM DUAL;

select * from products;

select CATEGORYID from products;

select COUNT(DISTINCT(CATEGORYID)) from products;


SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;


SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT COUNT(*)
FROM Products;

SELECT COUNT(ProductName)
FROM Products;

SELECT COUNT(DISTINCT(ProductName))
FROM Products;

SELECT COUNT(DISTINCT Price)
FROM Products;

SELECT COUNT(ProductID)
FROM Products
WHERE Price > 20;


SELECT COUNT(*) AS "Number of records"
FROM Products;

SELECT COUNT(*) AS "Number of records",CategoryID
FROM Products
Group By CategoryId
order by Count(*) ASC;


CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);

INSERT ALL  
INTO OrderDetails VALUES (1, 10248, 11, 12)
INTO OrderDetails VALUES (2, 10248, 42, 10)
INTO OrderDetails VALUES (3, 10248, 72, 5)
INTO OrderDetails VALUES (4, 10249, 14, 9)
INTO OrderDetails VALUES (5, 10249, 51, 40)
INTO OrderDetails VALUES (6, 10250, 41, 10)
INTO OrderDetails VALUES (7, 10250, 51, 35)
SELECT * FROM DUAL;


SELECT SUM(Quantity)
FROM OrderDetails;

SELECT SUM(Quantity)
FROM OrderDetails
WHERE ProductId = 11;

SELECT SUM(Quantity) AS total
FROM OrderDetails;

SELECT OrderID, SUM(Quantity) AS "Total Quantity"
FROM OrderDetails
GROUP BY OrderID;

SELECT SUM(Quantity * 10)
FROM OrderDetails;

SELECT SUM(Price * Quantity) AS BILL
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID != Products.ProductID;

SELECT SUM(Price * Quantity) AS BILL
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;

SELECT AVG(Price)
FROM Products;

SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;

SELECT AVG(Price) as "AVG PRICE"
FROM Products
WHERE CategoryID = 1;


SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);


SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;

SELECT * FROM Customers
WHERE CustomerName LIKE 'A%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%A%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%a%';

SELECT Country FROM Customers
WHERE Country LIKE 'C%a';

SELECT country FROM Customers
WHERE country LIKE '%l%';


SELECT country FROM Customers
WHERE country LIKE 'Ca%';

SELECT CustomerName FROM Customers
WHERE CustomerName LIKE 'A%' OR CustomerName LIKE 'B%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'A__%';


--8 characters and above starts with A
SELECT * FROM Customers
WHERE CustomerName LIKE 'A________%';

SELECT * FROM Customers
WHERE Country LIKE 'Canada';

select * from customers;

SELECT * FROM Customers
WHERE CustomerName LIKE '[A-Z]%';

SELECT * FROM Customers
WHERE Country IN ('California', 'Canada', 'UK');


SELECT * FROM Customers
WHERE Country NOT IN ('California', 'Canada', 'UK');

select * from OrderDetails;

SELECT * FROM CUSTOMERS;

SELECT * FROM Customers,OrderDetails
WHERE CustomerID IN (SELECT CustomerID FROM OrderDetails);

SELECT Distinct(Customername) FROM Customers,OrderDetails
WHERE CustomerID IN (SELECT CustomerID FROM OrderDetails);

SELECT * FROM Customers,OrderDetails
WHERE CustomerID NOT IN (SELECT CustomerID FROM OrderDetails);

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID IN (1,2,3);

SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;

SELECT ProductName AS "My Great Products"
FROM Products;


desc customers;

SELECT CustomerName, (Address || ', ' || PostalCode || ' ' || City || ', ' || Country) AS Address
FROM Customers;

-------------------------------------------------------------------------------------------------
select * from customers;

select * from employee;

select * from department;

INSERT ALL
INTO department (deptid, deptname, deptcode, deptloc) VALUES (101, 'Human Resources', 'HR', 'New York')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (102, 'Finance', 'FIN', 'London')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (103, 'IT', 'IT', 'San Francisco')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (104, 'Marketing', 'MKT', 'Chicago')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (105, 'Sales', 'SLS', 'Boston')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (106, 'Research', 'RES', 'Berlin')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (107, 'Customer Support', 'CS', 'Toronto')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (108, 'Logistics', 'LOG', 'Los Angeles')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (109, 'Procurement', 'PRC', 'Tokyo')
INTO department (deptid, deptname, deptcode, deptloc) VALUES (110, 'Legal', 'LGL', 'Paris')
SELECT * FROM dual;

CREATE TABLE products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT ALL 
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(1, 'Chais', 1, 1, '10 boxes x 20 bags', 18.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(6, 'Grandma''s Boysenberry Spread', 3, 2, '12 - 8 oz jars', 25.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(7, 'Uncle Bob''s Organic Dried Pears', 3, 7, '12 - 1 lb pkgs.', 30.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(8, 'Northwoods Cranberry Sauce', 3, 2, '12 - 12 oz jars', 40.00)
INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97.00)
SELECT * FROM DUAL;

select * from products;

select CATEGORYID from products;

select COUNT(DISTINCT(CATEGORYID)) from products;


SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;


SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT COUNT(*)
FROM Products;

SELECT COUNT(ProductName)
FROM Products;

SELECT COUNT(DISTINCT(ProductName))
FROM Products;

SELECT COUNT(DISTINCT Price)
FROM Products;

SELECT COUNT(ProductID)
FROM Products
WHERE Price > 20;


SELECT COUNT(*) AS "Number of records"
FROM Products;

SELECT COUNT(*) AS "Number of records",CategoryID
FROM Products
Group By CategoryId
order by Count(*) ASC;


CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);

INSERT ALL  
INTO OrderDetails VALUES (1, 10248, 11, 12)
INTO OrderDetails VALUES (2, 10248, 42, 10)
INTO OrderDetails VALUES (3, 10248, 72, 5)
INTO OrderDetails VALUES (4, 10249, 14, 9)
INTO OrderDetails VALUES (5, 10249, 51, 40)
INTO OrderDetails VALUES (6, 10250, 41, 10)
INTO OrderDetails VALUES (7, 10250, 51, 35)
SELECT * FROM DUAL;


SELECT SUM(Quantity)
FROM OrderDetails;

SELECT SUM(Quantity)
FROM OrderDetails
WHERE ProductId = 11;

SELECT SUM(Quantity) AS total
FROM OrderDetails;

SELECT OrderID, SUM(Quantity) AS "Total Quantity"
FROM OrderDetails
GROUP BY OrderID;

SELECT SUM(Quantity * 10)
FROM OrderDetails;

SELECT SUM(Price * Quantity) AS BILL
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID != Products.ProductID;

SELECT SUM(Price * Quantity) AS BILL
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;

SELECT AVG(Price)
FROM Products;

SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;

SELECT AVG(Price) as "AVG PRICE"
FROM Products
WHERE CategoryID = 1;


SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);


SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;

SELECT * FROM Customers
WHERE CustomerName LIKE 'A%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%A%';

SELECT * FROM Customers
WHERE CustomerName LIKE '%a%';

SELECT Country FROM Customers
WHERE Country LIKE 'C%a';

SELECT country FROM Customers
WHERE country LIKE '%l%';


SELECT country FROM Customers
WHERE country LIKE 'Ca%';

SELECT CustomerName FROM Customers
WHERE CustomerName LIKE 'A%' OR CustomerName LIKE 'B%';

SELECT * FROM Customers
WHERE CustomerName LIKE 'A__%';


--8 characters and above starts with A
SELECT * FROM Customers
WHERE CustomerName LIKE 'A________%';

SELECT * FROM Customers
WHERE Country LIKE 'Canada';

select * from customers;

SELECT * FROM Customers
WHERE CustomerName LIKE '[A-Z]%';

SELECT * FROM Customers
WHERE Country IN ('California', 'Canada', 'UK');


SELECT * FROM Customers
WHERE Country NOT IN ('California', 'Canada', 'UK');

select * from OrderDetails;

SELECT * FROM CUSTOMERS;

SELECT * FROM Customers,OrderDetails
WHERE CustomerID IN (SELECT CustomerID FROM OrderDetails);

SELECT Distinct(Customername) FROM Customers,OrderDetails
WHERE CustomerID IN (SELECT CustomerID FROM OrderDetails);

SELECT * FROM Customers,OrderDetails
WHERE CustomerID NOT IN (SELECT CustomerID FROM OrderDetails);

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID IN (1,2,3);

SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;

SELECT ProductName AS "My Great Products"
FROM Products;


desc customers;

SELECT CustomerName, (Address || ', ' || PostalCode || ' ' || City || ', ' || Country) AS Address
FROM Customers;














