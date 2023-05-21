/*
DDL = Database Definition Language = instructiunile prin care definim structura
bazei de date:
1. CREATE
2. DROP
3. ALTER
4. RENAME
*/

-- asa se pot scrie comentarii in limbajul SQL
/*
Multiline comment.
*/
create database if not exists curs; -- creaza o baza de date (daca nu exista deja)
use curs;	-- seteaza baza de date "curs" ca fiind cea pe care lucram in mod curent

CREATE TABLE Company (
    ID INT NOT NULL,
    CompanyName VARCHAR(127) NOT NULL,
    Address VARCHAR(255),
    Capital INT,
    PRIMARY KEY (ID)
);
/*
FOREIGN KEY = modalitatea prin care un tabel poate avea o relatie cu un alt tabel
Zicem ca tabelul A referentiaza tabelul B, si folosim urmatoarea sintaxa.
FOREIGN KEY (CheieTabelA) REFERENCES TabelB(CheieTabelB), cu conditia ca
CheieTabelB sa fie not null si unique (sau primary key).
*/

CREATE TABLE Employee (
    CNP VARCHAR(13) NOT NULL,
    FirstName VARCHAR(31),
    LastName VARCHAR(31),
    EmploymentDate DATE,
    BirthDate DATE,
    CompanyID INT,
    PRIMARY KEY (CNP),
    FOREIGN KEY (CompanyID)
        REFERENCES Company (ID)
);

/*
ALTER  - instructiune care ne permite sa modificam structura unui element (db sau tabel).
Avem mai multe tipuri de actiuni (pe tabel):
- RENAME table/column TO new_table/new_column
- ADD column
- DROP column
- MODIFY column
*/

ALTER TABLE Company ADD COLUMN IsSRL BOOL DEFAULT True;

/*
Pentru a manipula datele din interiorul bazei noastre de date, folosim urmatoarele instructiuni:
- INSERT - cream o intrare noua in db (adica un row)
- UPDATE - modificam un row (ATENTIE, aici avem de obicei nevoie de WHERE!!!)
- DELETE - stergem un row (ATENTIE, aici avem nevoie de WHERE)
*/

INSERT INTO Company (ID, CompanyName, Address, Capital)
VALUES 	(1, "Apple", "Silicon Valley", 10000000),
		(2, "Microsoft", "Bucuresti", 150000),
		(3, "Emag", "Romania", 250000);

INSERT INTO Employee (CNP, FirstName, EmploymentDate, CompanyID)
VALUES ('12345678901', "Marcela", "2020-03-01", 1);

UPDATE Employee
SET
    LastName = 'Ionescu',
    BirthDate = '1991-05-12'
WHERE
    CNP = '123456';

DELETE FROM Employee
WHERE
    CNP = '1234567';