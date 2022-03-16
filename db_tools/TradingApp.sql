--
-- ER/Studio Data Architect SQL Code Generation
-- Project :      ModeloER_TradingApp.DM1
--
-- Date Created : Tuesday, March 15, 2022 16:18:31
-- Target DBMS : MySQL 5.x
--

-- 
-- TABLE: tbl_Country 
--

USE billionsdb;

CREATE TABLE tbl_Country(
    idCountry      INT            AUTO_INCREMENT,
    countryName    VARCHAR(50)    NOT NULL,
    PRIMARY KEY (idCountry)
)ENGINE=INNODB
;



-- 
-- TABLE: tbl_Exchange 
--

CREATE TABLE tbl_Exchange(
    idExchange      INT            AUTO_INCREMENT,
    exchangeName    VARCHAR(50)    NOT NULL,
    idCountry       INT            NOT NULL,
    PRIMARY KEY (idExchange)
)ENGINE=INNODB
;



-- 
-- TABLE: tbl_Ticker 
--

CREATE TABLE tbl_Ticker(
    idTicker      INT             AUTO_INCREMENT,
    symbol        VARCHAR(25)     NOT NULL,
    company       VARCHAR(255)    NOT NULL,
    currency      VARCHAR(3)      NOT NULL,
    idExchange    INT             NOT NULL,
    PRIMARY KEY (idTicker)
)ENGINE=INNODB
;



-- 
-- TABLE: tbl_tickerPrice 
--

CREATE TABLE tbl_tickerPrice(
    idTickerPrice    INT            AUTO_INCREMENT,
    idTicker         INT            NOT NULL,
    Date             DATETIME       NOT NULL,
    openPrice        FLOAT(8, 0)    NOT NULL,
    dailyHigh        FLOAT(8, 0)    NOT NULL,
    dailyLow         FLOAT(8, 0)    NOT NULL,
    closePrice       FLOAT(8, 0)    NOT NULL,
    AveragePrice     FLOAT(8, 0)    NOT NULL,
    PRIMARY KEY (idTickerPrice)
)ENGINE=INNODB
;



-- 
-- INDEX: Ref21 
--

CREATE INDEX Ref21 ON tbl_Exchange(idCountry)
;
-- 
-- INDEX: Ref32 
--

CREATE INDEX Ref32 ON tbl_Ticker(idExchange)
;
-- 
-- INDEX: Ref13 
--

CREATE INDEX Ref13 ON tbl_tickerPrice(idTicker)
;
-- 
-- TABLE: tbl_Exchange 
--

ALTER TABLE tbl_Exchange ADD CONSTRAINT Reftbl_Country1 
    FOREIGN KEY (idCountry)
    REFERENCES tbl_Country(idCountry)
;


-- 
-- TABLE: tbl_Ticker 
--

ALTER TABLE tbl_Ticker ADD CONSTRAINT Reftbl_Exchange2 
    FOREIGN KEY (idExchange)
    REFERENCES tbl_Exchange(idExchange)
;


-- 
-- TABLE: tbl_tickerPrice 
--

ALTER TABLE tbl_tickerPrice ADD CONSTRAINT Reftbl_Ticker3 
    FOREIGN KEY (idTicker)
    REFERENCES tbl_Ticker(idTicker)
;


