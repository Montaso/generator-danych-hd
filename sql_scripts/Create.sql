CREATE TABLE U¿ytkownicy (
    ID_u¿ytkownika INT PRIMARY KEY,
    Imiê VARCHAR(50) NOT NULL CHECK(LEN(Imiê) <= 50),
    Nazwisko VARCHAR(50) NOT NULL CHECK(LEN(Nazwisko) <= 50),
    Data_Urodzenia DATE NOT NULL CHECK(LEN(Data_Urodzenia) = 10),
    Data_Rejestracji DATE NOT NULL CHECK(LEN(Data_Rejestracji) = 10)
);

CREATE TABLE Stacje (
    ID_stacji INT PRIMARY KEY,
    Szerokosc_geograficzna DECIMAL(10, 6) NOT NULL,
    Dlugosc_geograficzna DECIMAL(10, 6) NOT NULL,
    Liczba_miejsc INT NOT NULL CHECK(Liczba_miejsc > 0 AND Liczba_miejsc < 50),
    Czy_Aktualna BIT NOT NULL
);

CREATE TABLE Pojazdy (
    ID_pojazdu INT PRIMARY KEY,
    Typ VARCHAR(10) CHECK (Typ IN ('bicycle', 'scooter')) NOT NULL,
    Elektryczny BIT NOT NULL,
    Data_zakupu DATE NOT NULL CHECK(LEN(Data_zakupu) = 10),
    Moc_silnika INT NOT NULL CHECK(Moc_silnika >= 250  AND Moc_silnika <= 1500),
    Pojemnosc_akumulatora INT NOT NULL CHECK(Pojemnosc_akumulatora >= 500  AND Pojemnosc_akumulatora <= 1000),
    Czy_nadal_uzywany BIT NOT NULL
);

CREATE TABLE Wypo¿yczenia (
    ID_wypo¿yczenia INT PRIMARY KEY,
    FK_ID_pojazdu INT NOT NULL,
    FK_ID_uzytkownika INT NOT NULL,
    Koszt DECIMAL(10, 2) NOT NULL CHECK(Koszt > 0),
    Czas_wypozyczenia INT NOT NULL CHECK(Czas_wypozyczenia > 0),
    Przejechany_dystans INT CHECK(Przejechany_dystans > 0),
    FK_Stacja_startowa INT,
    FK_Stacja_koncowa INT,
    Poprawne_odstawienie BIT NOT NULL,
    Data_startu DATE NOT NULL CHECK(LEN(Data_startu) = 10),

    FOREIGN KEY (FK_ID_pojazdu) REFERENCES Pojazdy(ID_pojazdu),
    FOREIGN KEY (FK_ID_uzytkownika) REFERENCES u¿ytkownicy(ID_u¿ytkownika),
    FOREIGN KEY (FK_Stacja_startowa) REFERENCES Stacje(ID_stacji),
    FOREIGN KEY (FK_Stacja_koncowa) REFERENCES Stacje(ID_stacji)
);
