Create DataBase Etapa3;
USE Etapa3;

CREATE TABLE CompanyProfiles(
    Symbol Varchar(255),
    Company varchar(255),
    Sector varchar(255),
    Headquarters varchar(255),
    Fechafundada varchar(255)
);

CREATE TABLE Companies(
    Date Date,
    Symbol varchar(255),
    Cierre Float
);

--Eliminar Columna
--ALTER TABLE Companies
--DROP COLUMN Company;


ALTER TABLE CompanyProfiles
ALTER COLUMN Symbol Varchar NOT NULL;

ALTER TABLE CompanyProfiles
ADD CONSTRAINT PK_Symbol PRIMARY KEY (Symbol);

ALTER TABLE Companies
ALTER COLUMN Date Date NOT NULL;

ALTER TABLE Companies
ALTER COLUMN Symbol Varchar NOT NULL;

ALTER TABLE Companies
ADD CONSTRAINT PK_Companies PRIMARY KEY (Date, Symbol);

select * from Companies;
select * from CompanyProfiles;
