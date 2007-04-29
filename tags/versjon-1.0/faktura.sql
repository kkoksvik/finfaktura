-- ###########################################################################
-- #    Copyright (C) 2005-2006 - Håvard Dahle og Håvard Sjøvoll
-- #    <havard@dahle.no>, <sjovoll@ntnu.no>
-- #
-- #    GPL version 2
-- #
-- # $Id$
-- ###########################################################################
--
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
        
    -- Versjon 2.7
    CREATE TABLE Epost (ID INTEGER PRIMARY KEY,
        bcc UNICODE,
        transport INT DEFAULT 0,
        gmailbruker UNICODE,
        gmailpassord UNICODE,
        smtpserver UNICODE,
        smtpport INT DEFAULT 25,
        smtptls INT DEFAULT 0,
        smtpauth INT DEFAULT 0,
        smtpbruker UNICODE,
        smtppassord UNICODE,
        sendmailsti UNICODE);
    
    -- Versjon 2.9
    DELETE FROM Handling;
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'opprettet');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'forfalt');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'markertForfalt');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'purret'    );
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'betalt'    );
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'kansellert');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'avKansellert');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'sendtTilInkasso');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'utskrift');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'epostSendt');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'epostSendtSmtp');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'epostSendtGmail');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'epostSendtSendmail');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'pdfEpost');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'pdfPapir');
    INSERT INTO Handling (ID, navn) VALUES (NULL, 'pdfSikkerhetskopi');

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    DELETE FROM Oppsett;
    INSERT INTO Oppsett (ID, databaseversjon, fakturakatalog) VALUES (1, 2.9, '~');
