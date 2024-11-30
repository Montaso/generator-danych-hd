use Przejazd

CREATE TABLE Uzytkownicy (
    ID_uzytkownika INT PRIMARY KEY,
    Imie VARCHAR(50) NOT NULL CHECK(LEN(Imie) <= 50),
    Nazwisko VARCHAR(50) NOT NULL CHECK(LEN(Nazwisko) <= 50),
    Data_Urodzenia DATE NOT NULL CHECK(LEN(Data_Urodzenia) = 10),
    Data_Rejestracji DATE NOT NULL CHECK(LEN(Data_Rejestracji) = 10),
	PESEL VARCHAR(11) UNIQUE CHECK (ISNUMERIC(PESEL) = 1 AND LEN(PESEL) = 11)
);

CREATE TABLE Stacje (
    ID_stacji INT PRIMARY KEY,
    Szerokosc_geograficzna DECIMAL(10, 6) NOT NULL,
    Dlugosc_geograficzna DECIMAL(10, 6) NOT NULL,
    Czy_Aktualna BIT NOT NULL,
    Liczba_miejsc INT NOT NULL CHECK(Liczba_miejsc > 0 AND Liczba_miejsc < 50),
	Nazwa varchar(20) NOT NULL
);

CREATE TABLE Pojazdy (
    ID_pojazdu INT PRIMARY KEY,
    Typ VARCHAR(10) CHECK (Typ IN ('bicycle', 'scooter')) NOT NULL,
    Elektryczny BIT NOT NULL,
    Data_zakupu DATE NOT NULL CHECK(LEN(Data_zakupu) = 10),
    Moc_silnika INT NOT NULL CHECK(Moc_silnika >= 250  AND Moc_silnika <= 1500),
    Czy_nadal_uzywany BIT NOT NULL,
    Pojemnosc_akumulatora INT NOT NULL CHECK(Pojemnosc_akumulatora >= 500  AND Pojemnosc_akumulatora <= 1000),
	Nazwa varchar(20) NOT NULL
);

CREATE TABLE Wypozyczenia (
    ID_wypozyczenia INT PRIMARY KEY,
    FK_Stacja_startowa INT,
    FK_Stacja_koncowa INT,
    Koszt DECIMAL(10, 2) NOT NULL CHECK(Koszt > 0),
    Czas_wypozyczenia INT NOT NULL CHECK(Czas_wypozyczenia > 0),
    Przejechany_dystans INT CHECK(Przejechany_dystans > 0),
    FK_ID_pojazdu INT NOT NULL,
    FK_ID_uzytkownika INT NOT NULL,
    Poprawne_odstawienie BIT NOT NULL,
    Data_startu DATE NOT NULL,
    Czas_startu TIME NOT NULL

    FOREIGN KEY (FK_ID_pojazdu) REFERENCES Pojazdy(ID_pojazdu),
    FOREIGN KEY (FK_ID_uzytkownika) REFERENCES uzytkownicy(ID_uzytkownika),
    FOREIGN KEY (FK_Stacja_startowa) REFERENCES Stacje(ID_stacji),
    FOREIGN KEY (FK_Stacja_koncowa) REFERENCES Stacje(ID_stacji)
);

CREATE TABLE Vany (
    Numer_rejestracji VARCHAR(7) PRIMARY KEY,
    Czy_nadal_uzywany BIT NOT NULL,
    Pojemnosc INT CHECK (Pojemnosc >= 5000000 AND Pojemnosc <= 20000000) NOT NULL  -- Van capacity in cm^3
);

CREATE TABLE Kierowcy (
    ID_kierowcy INT PRIMARY KEY,
    PESEL VARCHAR(11) CHECK (ISNUMERIC(PESEL) = 1 AND LEN(PESEL) = 11),
    Imie VARCHAR(20) NOT NULL,
    Nazwisko VARCHAR(20) NOT NULL,
    Czy_nadal_pracuje BIT NOT NULL,
    Data_zatrudnienia DATE CHECK (Data_zatrudnienia <= GETDATE()) NOT NULL
);

CREATE TABLE Trasy_Vanow (
    ID_trasy INT PRIMARY KEY,
    FK_ID_kierowcy INT NOT NULL,
    FK_Numer_rejestracji_vana VARCHAR(7) NOT NULL,
    Data_trasy DATE CHECK (Data_trasy <= GETDATE()),
    FOREIGN KEY (FK_ID_kierowcy) REFERENCES Kierowcy(ID_kierowcy),
    FOREIGN KEY (FK_Numer_rejestracji_vana) REFERENCES Vany(Numer_rejestracji)
);

CREATE TABLE Wymiany_Akumulatorow (
    ID_wymiany INT PRIMARY KEY,
    FK_ID_trasy INT NOT NULL,
    FK_ID_pojazdu INT NOT NULL,
    FOREIGN KEY (FK_ID_pojazdu) REFERENCES Pojazdy(ID_pojazdu),
    FOREIGN KEY (FK_ID_trasy) REFERENCES Trasy_Vanow(ID_trasy)
);
