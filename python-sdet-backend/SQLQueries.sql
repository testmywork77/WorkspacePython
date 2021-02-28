/*
CREATE DATABASE PythonAutomation;
CREATE DATABASE APIDevelop;
*/

-- USE APIDevelop;
USE PythonAutomation;

-- Create Table Script
CREATE TABLE User
(
	Name varchar(50),
	Job varchar(50)	
);
-- Insert Scripts
INSERT INTO User VALUES('Venkat','Developer');
INSERT INTO User VALUES('Babu','Tester');
INSERT INTO User VALUES('Ram','DevOps');

-- Create Table Script
CREATE TABLE CustomerInfo
(
	CourseName varchar(50),
	PurchasedDate date,
	Amount int,
	Location varchar(50)
);
-- Insert Scripts
INSERT INTO CustomerInfo VALUES("selenium",CURRENT_DATE(),120,'Africa');
INSERT INTO CustomerInfo VALUES("Protractor",CURRENT_DATE(),45,'Africa');
INSERT INTO CustomerInfo VALUES("Appium",CURRENT_DATE(),99,'Asia');
INSERT INTO CustomerInfo VALUES("WebServices",CURRENT_DATE(),21,'Asia');
INSERT INTO CustomerInfo VALUES("Jmeter",CURRENT_DATE(),76,'Asia');

-- Create Table Script
CREATE TABLE Books
(
	BookName varchar(50),
	isbn varchar(50),
	aisle varchar(50),
	author varchar(50)
);
-- Insert Scripts
INSERT INTO Books VALUES("Devops","bnid34","75","Rahul Shetty2");
INSERT INTO Books VALUES("Selenium","kosncs34fr","23","Rahul Shetty");
INSERT INTO Books VALUES("Jmeter","rtbrss24t","234","Rahul Shetty3");

SELECT * FROM Books;
SELECT * FROM CustomerInfo;

/*
SET SQL_SAFE_UPDATES = 0;
UPDATE customerInfo SET Location = 'US' WHERE CourseName = 'Jmeter';
DELETE FROM customerInfo WHERE courseName = 'WebServices';

CREATE TABLE Storage3
(
	book_name varchar(50),id varchar(50),
	isbn varchar(50),
	aisle int,
	author varchar(50),PRIMARY KEY (id)
);

INSERT INTO Storage3(book_name,id,isbn,aisle,author) VALUES("Appium","fdsefr343","fdsefr3","43","Rahul Shetty");
INSERT INTO Storage3 VALUES("selenium","qwer12","qwer","12","Rahul Shetty");

SELECT * FROM Storage3;
*/

USE pythonautomation;
SELECT * FROM User
-- SELECT * FROM books;
-- SELECT * FROM customerinfo