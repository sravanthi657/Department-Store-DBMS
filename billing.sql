DROP DATABASE IF EXISTS billing;
create database billing;
use billing;

drop table if exists CUSTOMER;
drop table if exists MEMBER;
drop table if exists NON_MEMBER;
drop table if exists MEMBERSHIP;
drop table if exists ADMIN;
drop table if exists PRODUCT;
drop table if exists SALE;
drop table if exists PRODUCTS_OF_SALE;
drop table if exists BILL;

create table ADMIN(
Admin_ID INT(11) NOT NULL,
Date_On DATE NOT NULL,
Time_at TIME  NOT NULL,
Reported_Admin_ID INT NOT NULL,
CONSTRAINT KEEY PRIMARY KEY (Admin_ID,Date_On),
CONSTRAINT master FOREIGN KEY (Reported_Admin_ID) REFERENCES ADMIN(Admin_ID)
);
insert into ADMIN VALUES
(7652389,'2019-09-20','18:58:08',7652389),
(5439167,'2019-09-09','18:58:08',7652389),
(1234453,'2019-09-15','18:58:08',5439167),
(7652389,'2019-09-28','18:58:08',7652389);
create table CUSTOMER(
First_Name varchar(30) NOT NULL,
Last_Name varchar(30) NOT NULL,
Email_ID varchar(60) NOT NULL,
Mobile_Number bigint NOT NULL,
Admin_Assisstance_Feedback  ENUM('0','1','2','3','4','5') DEFAULT '5', 
CONSTRAINT ch CHECK((Admin_Assisstance_Feedback)>=0 AND (Admin_Assisstance_Feedback)<=5),
Date_of_Birth DATE NOT NULL,
Admin_ID INT NOT NULL,
PRIMARY KEY (Mobile_Number),
FOREIGN KEY (Admin_ID) REFERENCES ADMIN(Admin_ID),
UNIQUE (Email_ID)
);
INSERT into CUSTOMER VALUES 
	('John','Doe','abcd12@gmail.com','9988345673',2,'1987-09-05',7652389),
('Jane','Doe','efgh710@fmail.com','9384725644',5,'2000-11-01',1234453),
('Jack','Sparrow','jackkie.spa@hotmail.com','9654378412',3,'1975-12-12',1234453),
('Rick','Sanchez','rick_sanchez@outlook.com','8729562543',4,'2003-06-28',5439167),
('Spike','Spiegel','space.cowboy@hotmail.com','9657358412',5,'2001-04-16',5439167);

create table MEMBER(
Mobile_Number bigint NOT NULL,
Membership_ID int NOT NULL DEFAULT 0,
CONSTRAINT mem_key PRIMARY KEY (Mobile_Number,Membership_ID), 
FOREIGN KEY (Mobile_Number) REFERENCES CUSTOMER(Mobile_Number),
UNIQUE(Membership_ID)
);
INSERT into MEMBER VALUES
(8729562543,1133),
(9654378412,3247),
(9657358412,1274);

create table NON_MEMBER(
Mobile_Number bigint NOT NULL,
Points_Redeemed int NOT NULL DEFAULT 0,
Points_Active int NOT NULL DEFAULT 0,
PRIMARY KEY (Mobile_Number),
FOREIGN KEY (Mobile_Number) REFERENCES CUSTOMER(Mobile_Number)
);
INSERT into NON_MEMBER VALUES
(9988345673,250,750),
(9384725644,1000,320);

create table MEMBERSHIP(
Membership_ID int NOT NULL,
Points_Redeemed int NOT NULL DEFAULT 0,
Membership_Points int NOT NULL DEFAULT 0,
PRIMARY KEY (Membership_ID),
FOREIGN KEY (Membership_ID) REFERENCES MEMBER(Membership_ID)
);
INSERT into MEMBERSHIP VALUES
(1133,630,70),
(1274,300,40),
(3247,540,50);


create table PRODUCT(
Product_ID int NOT NULL,
Price_per_Unit int(11) unsigned DEFAULT 0,
Unit ENUM('litres','kilograms','dozens', 'units'),
Admin_ID int NOT NULL,
UNIQUE(Product_ID),
PRIMARY KEY (Product_ID),
FOREIGN KEY (Admin_ID) REFERENCES ADMIN(Admin_ID)
);
INSERT into PRODUCT VALUES
(101,50,'litres',7652389),
(102,60,'kilograms',5439167),
(103,30,'dozens',1234453),
(104,40,'units',5439167),
(105,70,'kilograms',7652389);

create table PAYMENT(
Customer_Mobile bigint NOT NULL,
Payment_ID int NOT NULL,
Mode_of_Payment ENUM('Cash','Debit Card','Credit Card','UPI') NOT NULL,
Amount_Paid int(10) NOT NULL,
Balance int(10) DEFAULT 0,
UNIQUE(Payment_ID),
CONSTRAINT pay_key PRIMARY KEY (Customer_Mobile,Payment_ID),
FOREIGN KEY (Customer_Mobile) REFERENCES CUSTOMER(Mobile_Number)
);
INSERT into PAYMENT VALUES
(9988345673,201,'Cash',1000,50),
(9988345673,206,'UPI',1000,50),
(9384725644,202,'UPI',400,0),
(9654378412,203,'Debit Card',400,0),
(8729562543,204,'Cash',200,10),
(9657358412,205,'UPI',700,0);

create table SALE(
Customer_Mobile bigint NOT NULL,
SALE_ID int NOT NULL,
Amount int(10) NOT NULL,
Payment_ID int NOT NULL,
UNIQUE(Sale_ID),
CONSTRAINT sale_key PRIMARY KEY (Customer_Mobile,Sale_ID),
FOREIGN KEY (Customer_Mobile) REFERENCES CUSTOMER(Mobile_Number),
FOREIGN KEY (Payment_ID) REFERENCES PAYMENT(Payment_ID)
);
INSERT into SALE VALUES
(9988345673,401,950,201),
(9384725644,402,400,202),
(9654378412,403,400,203),
(8729562543,404,190,204),
(9657358412,405,700,205);

create table PRODUCTS_OF_SALE(
Customer_Mobile bigint NOT NULL,
SALE_ID int NOT NULL,
Sale_Products varchar(30) NOT NULL,
CONSTRAINT ps_key PRIMARY KEY (Customer_Mobile,Sale_ID,Sale_Products),
FOREIGN KEY (Customer_Mobile) REFERENCES CUSTOMER(Mobile_Number),
FOREIGN KEY (Sale_ID) REFERENCES SALE(Sale_ID)
);
INSERT into PRODUCTS_OF_SALE VALUES
(9988345673,401,'Milk'),
(9988345673,401,'Rice'),
(9384725644,402,'Wheat'),
(9384725644,402,'Apples'),
(9654378412,403,'Chart paper'),
(8729562543,404,'Milk'),
(8729562543,404,'Rice'),
(8729562543,404,'Wheat'),
(9657358412,405,'Apples'),
(9657358412,405,'Milk');

create table BILL(
Customer_Mobile bigint NOT NULL,
SALE_ID int NOT NULL,
Admin_ID int NOT NULL,
Product_ID int NOT NULL,
CONSTRAINT bill_key PRIMARY KEY (Customer_Mobile,Sale_ID,Admin_ID,Product_ID),
FOREIGN KEY (Admin_ID) REFERENCES ADMIN(Admin_ID),
FOREIGN KEY (Customer_Mobile) REFERENCES CUSTOMER(Mobile_Number),
FOREIGN KEY (Sale_ID) REFERENCES SALE(Sale_ID),
FOREIGN KEY (Product_ID) REFERENCES PRODUCT(Product_ID)
);
INSERT into BILL VALUES
(9988345673,401,7652389,101),
(9384725644,402,1234453,102),
(9654378412,403,1234453,103),
(8729562543,404,5439167,104),
(9657358412,405,5439167,105);

