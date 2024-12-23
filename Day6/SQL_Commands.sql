SELECT lower('Oracle') FROM dual;
SELECT instr('Oracle','a') FROM dual;
SELECT concat('Oracle','for') FROM dual;
SELECT concat(concat('Oracle',' for'),' developers') FROM dual;
SELECT substr('Oracle',2) FROM dual;
SELECT substr('Oracle',2,2) FROM dual;
SELECT length('Oracle for Developers') FROM dual;
SELECT ltrim('    Oracle for Developers') FROM dual;
SELECT rtrim('    Oracle for Developers         ') FROM dual;
SELECT lpad('Oracle',10,'*') FROM dual;
SELECT ceil(24.567) FROM dual;
SELECT round(24.567) FROM dual;
SELECT trunc(24.567,1) FROM dual;
SELECT power(5,2) FROM dual;
SELECT sqrt(16) FROM dual;
SELECT ADD_MONTHS(sysdate,3) FROM dual;
SELECT MONTHS_BETWEEN(sysdate,'20-MAY-2024') FROM dual;
SELECT LAST_DAY(sysdate) FROM dual;
SELECT NEXT_DAY(sysdate,3) FROM dual;

SELECT NEXT_DAY(sysdate,'friday') FROM dual;

SELECT EXTRACT(year FROM sysdate) FROM dual;

SELECT EXTRACT(month FROM sysdate) FROM dual;

SELECT EXTRACT(day FROM sysdate) FROM dual;


create table students_data(
Name VARCHAR2(10) NOT NULL,
Age Number(3) NOT NULL,
Id Varchar2(20) NOT NULL
);

desc students_data;

create table students_data_pk(
Name VARCHAR2(10) NOT NULL,
Age Number(3) NOT NULL,
Id Varchar2(20) NOT NULL,
primary key(Id)
);

desc students_data_pk;


CREATE TABLE customers(
CustomerID number(10) not null,
CustomerName Varchar2(100),
ContactName Varchar2(50),
Address Varchar2(200),
City varchar2(20),
PostalCode varchar2(20),
Country varchar2(50)
);

DESC Customers;

INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (1,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');


INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (2,'Bardinal', 'Jerry B. Erichsen', 'ETYH 21', 'Asgatvc', '4007', 'Canada');

INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (3,'Aardinal', 'Ben10 B. Erichsen', 'Wr24 21', 'Stranger', '4008', 'Canada');

INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (4,'Dardinal', 'Dot B. Erichsen', 'Eskatgve 21', 'Avengers', '4009', 'California');


select * from customers;

alter table customers 
rename column address to CustomerAddress;

desc customers;

--INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
--VALUES (5,'asrDrdinal', 'werfbDot B. Erichsen', 'dfy Eskatgve 21', 'dy Avengers', '4010', 'California');

INSERT INTO Customers (CustomerID,CustomerName, ContactName, CustomerAddress, City, PostalCode, Country)
VALUES (5,'Dqwer ardinal', 'qwrt Dot B. Erichsen', 'sdfg Eskatgve 21', 'Adfgh vengers', '40010', 'US California');

select * from customers;

create table temp_customers as ( select * from customers);

desc temp_customers;

select * from temp_customers;

alter table customers
rename column CustomerAddress to Address;

INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (5,'B Dardinal', 'B Dot B. Erichsen', 'BEskatgve 21', 'Bvengers', '4011', 'ABC California');

select * from customers;

select count(*) from customers;

select sum(CustomerID) as SUM_ID from customers;

select avg(CustomerID) as AVG_ID from customers;

select MIN(CustomerID) as MIN_ID from customers;

select MAX(CustomerID) as MAX_ID from customers;

show tables;


INSERT INTO Customers VALUES (6,'13 Dqwer ardinal', 'rty qwrt Dot B. Erichsen', 'f sdfg Eskatgve 21', 'h Adfgh vengers', '4011', 'UK California');

select * from customers;

truncate table temp_customers;

desc temp_customers;

drop table temp_customers;

--desc temp_customers;

create table temp_customers as ( select * from customers);

select * from temp_customers;

drop table temp_customers;

SELECT CustomerName, City FROM Customers;

SELECT * FROM Customers;

SELECT DISTINCT Country FROM Customers;

SELECT Country FROM Customers;

SELECT count(Country) FROM Customers;

SELECT count(Country) as Country_Count FROM Customers;

SELECT count(Distinct Country) FROM Customers;

SELECT count(Distinct Country) as Distinct_Country_Count FROM Customers;

SELECT Count(*) AS DistinctCountriesCount
FROM (SELECT DISTINCT Country FROM Customers);

SELECT Count(*) AS CountriesCount
FROM (SELECT Country FROM Customers);

SELECT DISTINCT Country as DistinctCountries FROM Customers;

SELECT * FROM Customers
WHERE Country='Mexico';

SELECT * FROM Customers
WHERE Country='Canada';

SELECT * FROM Customers
WHERE CustomerID=1;

SELECT * FROM Customers
WHERE CustomerID=2;

SELECT * FROM Customers
WHERE CustomerID>3;

select * from customers
order by CustomerID DESC;


select * from customers
order by CustomerID DESC , PostalCode ASC;

SELECT *
FROM Customers
WHERE Country = 'California' AND CustomerName LIKE 'G%';

SELECT *
FROM Customers
WHERE Country = 'California' AND CustomerName LIKE 'D%';

SELECT *
FROM Customers
WHERE Country = 'California' OR CustomerName LIKE 'D%';

SELECT * FROM Customers
WHERE Country = 'California' AND CustomerName LIKE 'D%' OR CustomerName LIKE 'A%';

SELECT * FROM Customers
WHERE Country = 'California' AND (CustomerName LIKE 'D%' OR CustomerName LIKE 'A%');


SELECT *
FROM Customers
WHERE Country = 'California' OR Country = 'Canada';

SELECT * FROM Customers
WHERE Country likec'%US%' AND (CustomerName LIKE 'B%' OR CustomerName LIKE 'C%');

select * from customers;

select CustomerName,Country from customers
where country like '%C%';

SELECT CustomerName,Country FROM Customers
WHERE NOT Country = 'Spain';

SELECT CustomerName FROM Customers
WHERE CustomerName NOT LIKE 'A%';


SELECT CustomerName FROM Customers
WHERE CustomerName NOT LIKE '%A%';

SELECT CustomerName FROM Customers
WHERE CustomerName NOT LIKE '%aa%';

desc customers;

SELECT CustomerID,CustomerName FROM Customers
WHERE CustomerID NOT BETWEEN 10 AND 60;

SELECT CustomerID,City FROM Customers
WHERE City  IN ('Avengers', 'Bvengers');

SELECT CustomerID,City FROM Customers
WHERE City NOT IN ('Avengers', 'Bvengers');

SELECT * FROM Customers
WHERE NOT CustomerID > 50;

SELECT * FROM Customers
WHERE NOT CustomerID > 5;

alter table customers
add age number;

desc customers;

INSERT INTO Customers 
VALUES (11,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway',21);


select * from customers;


INSERT INTO Customers (CustomerID,CustomerName, City, Country)
VALUES (12,'Cardinal', 'Stavanger', 'Norway');

SELECT * FROM Customers;

INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (13,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
(14,'Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway');


INSERT INTO Customers (CustomerID,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
(15,'Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');

select * from customers;

SELECT CustomerName, Age
FROM Customers
WHERE Age IS NULL;

SELECT CustomerName, Age
FROM Customers
WHERE Age IS NOT NULL;

UPDATE Customers
SET Age=21 where age is null;

UPDATE Customers
SET Age=22 where age is not null and CustomerID = 1;

select * from customers;


