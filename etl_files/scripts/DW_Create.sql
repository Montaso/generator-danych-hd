USE PrzejazdDW


CREATE TABLE Uzytkownik (
    ID_uzytkownika INT IDENTITY(1,1) PRIMARY KEY,
    Imie_i_nazwisko VARCHAR(40) NOT NULL,
    PESEL CHAR(12) NOT NULL
);

CREATE TABLE Stacja (
    ID_stacji INT IDENTITY(1,1) PRIMARY KEY,
    Lokalizacja VARCHAR(20) NOT NULL,
    Wielkosc VARCHAR(20) NOT NULL,
    Czy_aktualna VARCHAR(3) NOT NULL,
    Nazwa VARCHAR(20) NOT NULL
);

CREATE TABLE Czas (
    ID_czasu INT  IDENTITY(1,1) PRIMARY KEY,
    Godzina TINYINT NOT NULL,
    Minuta TINYINT NOT NULL
);

CREATE TABLE Data (
    ID_daty INT IDENTITY(1,1) PRIMARY KEY,
    Dzien TINYINT NOT NULL,
    Miesiac TINYINT NOT NULL,
    Rok SMALLINT NOT NULL,
    Dzien_tygodnia VARCHAR(20) NOT NULL,
    Dzien_roboczy VARCHAR(3) NOT NULL,
    Wakacje VARCHAR(3) NOT NULL,
    Nazwa_miesiaca VARCHAR(20) NOT NULL
);

CREATE TABLE Junk (
    ID_junk INT IDENTITY (1,1) PRIMARY KEY,
    Typ_trasy VARCHAR(20) NOT NULL,
    Typ_sredniego_spalania VARCHAR(20) NOT NULL
);

CREATE TABLE Pojazd (
    ID_pojazdu INT IDENTITY(1,1) PRIMARY KEY,
    Typ VARCHAR(20) NOT NULL,
    Elektryczny VARCHAR(3) NOT NULL,
    Typ_pojemnosci_akumulatora VARCHAR(20) NOT NULL,
    Czy_nadal_uzywany VARCHAR(3) NOT NULL,
    Nazwa VARCHAR(20) NOT NULL,
	Data_dezaktywacji DATE
);

CREATE TABLE Wypozyczenie_Junk (
    ID_junk INT IDENTITY(1,1) PRIMARY KEY,
    Poprawne_odstawienie VARCHAR(3) NOT NULL,
	Powrot_do_tej_samej_stacji VARCHAR(3) NOT NULL
);

CREATE TABLE Wypozyczenie (
    ID_pojazdu INT NOT NULL,
    ID_uzytkownika INT NOT NULL,
    ID_stacja_startowa INT NOT NULL,
    ID_stacja_koncowa INT NOT NULL,
    ID_junk INT NOT NULL,
    ID_daty_startu INT NOT NULL,
    ID_czasu_startu INT NOT NULL,
    Koszt DECIMAL(10, 2) NOT NULL,
    Czas_wypozyczenia INT NOT NULL,
    Przejechany_dystans DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (ID_pojazdu, ID_uzytkownika, ID_daty_startu, ID_czasu_startu, ID_stacja_startowa, ID_stacja_koncowa, ID_junk),
    FOREIGN KEY (ID_pojazdu) REFERENCES Pojazd(ID_pojazdu),
    FOREIGN KEY (ID_uzytkownika) REFERENCES Uzytkownik(ID_uzytkownika),
    FOREIGN KEY (ID_stacja_startowa) REFERENCES Stacja(ID_stacji),
    FOREIGN KEY (ID_stacja_koncowa) REFERENCES Stacja(ID_stacji),
    FOREIGN KEY (ID_junk) REFERENCES Wypozyczenie_Junk(ID_junk),
    FOREIGN KEY (ID_daty_startu) REFERENCES Data(ID_daty),
    FOREIGN KEY (ID_czasu_startu) REFERENCES Czas(ID_czasu)
);

CREATE TABLE Wykonanie_Wymiany_Akumulatora (
    ID_daty_trasy INT NOT NULL,
    Nr_trasy INT NOT NULL,
    ID_czasu_zakonczenia_trasy INT NOT NULL,
    ID_pojazdu INT NOT NULL,
    ID_junk INT NOT NULL,
    PRIMARY KEY (ID_daty_trasy, Nr_trasy, ID_czasu_zakonczenia_trasy, ID_pojazdu, ID_junk),
    FOREIGN KEY (ID_daty_trasy) REFERENCES Data(ID_daty),
    FOREIGN KEY (ID_czasu_zakonczenia_trasy) REFERENCES Czas(ID_czasu),
    FOREIGN KEY (ID_pojazdu) REFERENCES Pojazd(ID_pojazdu),
    FOREIGN KEY (ID_junk) REFERENCES Junk(ID_junk)
);
