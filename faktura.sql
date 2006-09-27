-- ###########################################################################
-- #    Copyright (C) 2005-2006 - Håvard Dahle og Håvard Sjøvoll
-- #    <havard@dahle.no>, <sjovoll@ntnu.no>
-- #
-- #
-- # $Id: faktura.sql,v 1.16 2006/09/10 12:40:41 havardda Exp $
-- ###########################################################################
--
--1) ========= Lag databasene ===========================
--   CREATE DATABASE faktura;
--2) ========= Legg til brukere =========================
--3) ========= Legg brukerene til i databasen ===========
--4) ========= Committ endringer ========================
--   FLUSH PRIVILEGES;
--5) ========= Opprett tabellene ========================
--   USE faktura;

    -- Versjon 0.1
    CREATE TABLE Firma (ID INTEGER PRIMARY KEY,
    	firmanavn UNICODE NOT NULL,
    	kontaktperson UNICODE,
    	adresse UNICODE,
    	postnummer INT,
    	poststed UNICODE,
    	telefon UNICODE,
    	mobil UNICODE,
    	telefaks UNICODE,
        epost UNICODE,
        www UNICODE,
    	kontonummer UNICODE,
    	organisasjonsnummer UNICODE,
    	mva INT NOT NULL,
    	forfall INT NOT NULL,
    	vilkar UNICODE,
    	logo BLOB);
    --	PRIMARY KEY(ID));
    
    -- Versjon 0.1
    CREATE TABLE Kunde (ID INTEGER PRIMARY KEY,
        slettet INT,
    	navn UNICODE,
    	kontaktperson UNICODE,
    	adresse UNICODE,
    	postnummer INT,
    	poststed UNICODE,
    	telefon UNICODE,
    	telefaks UNICODE,
    	status UNICODE,
    	epost UNICODE);
    --	PRIMARY KEY(ID));
    	
    -- Versjon 0.1
    CREATE TABLE Vare (ID INTEGER PRIMARY KEY,
        slettet INT,
    	navn UNICODE,
    	detaljer UNICODE,
    	enhet UNICODE,
        mva INT,
    	pris FLOAT);
    --	PRIMARY KEY(ID));
    	
    -- Versjon 0.1
    CREATE TABLE Ordrehode (ID INTEGER PRIMARY KEY,
    	kundeID MEDIUMINT NOT NULL,
    	ordredato INT NOT NULL,
    	forfall INT NOT NULL,
    	tekst UNICODE,
        kansellert INT DEFAULT 0,
    	betalt INT DEFAULT 0);
    --	PRIMARY KEY(ID));
   	
    -- Versjon 0.1
    CREATE TABLE Ordrelinje (ID INTEGER PRIMARY KEY,
    	ordrehodeID MEDIUMINT NOT NULL,
    	vareID MEDIUMINT NOT NULL,
    	kvantum INT NOT NULL,
        mva INT NOT NULL,
    	enhetspris FLOAT NOT NULL);
    --	PRIMARY KEY(ID));
    
    -- Versjon 2.2
    CREATE TABLE Postnummer (postnummer INTEGER NOT NULL,
        poststed UNICODE );

    -- Versjon 2.0
    CREATE TABLE Oppsett (ID INTEGER,
        databaseversjon FLOAT NOT NULL,
        fakturakatalog UNICODE NOT NULL);
    
    -- Versjon 2.1
    CREATE TABLE Sikkerhetskopi (ID INTEGER PRIMARY KEY,
        ordreID INT NOT NULL,
        dato INT NOT NULL,
        data BLOB);

    -- Versjon 2.6
    CREATE TABLE Historikk (
        ordreID INT NOT NULL,
        dato INT NOT NULL,
        handlingID NOT NULL,
        suksess INT DEFAULT 0,
        forklaring UNICODE);
    
    -- Versjon 2.6
    CREATE TABLE Handling (ID INTEGER PRIMARY KEY,
        navn UNICODE NOT NULL,
        tekst UNICODE);
        
    	
--6) =============== Oppdater tabellene ==================
--7) ========= Sett inn default-verdier ==================
    INSERT INTO Oppsett (databaseversjon) VALUES (2.6);
