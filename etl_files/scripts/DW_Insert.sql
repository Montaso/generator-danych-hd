USE Przejazd

INSERT INTO Uzytkownik (ID_uzytkownika, Imie_i_nazwisko, PESEL) VALUES
(1, 'Jan Kowalski', '90010112345'),
(2, 'Anna Nowak', '85040567890'),
(3, 'Piotr Wiśniewski', '92031245678'),
(4, 'Maria Zielińska', '89070734567');

INSERT INTO Stacja (ID_stacji, Lokalizacja, Wielkosc, Czy_aktualna, Nazwa) VALUES
(1, 'Centrum miasta', 'Duża', 'Tak', 'Stacja A'),
(2, 'Przedmieścia', 'Średnia', 'Tak', 'Stacja B'),
(3, 'Obrzeża', 'Mała', 'Nie', 'Stacja C'),
(4, 'Wieś', 'Duża', 'Tak', 'Stacja D');

INSERT INTO Czas (ID_czasu, Godzina, Minuta) VALUES
(1, 8, 15),
(2, 12, 30),
(3, 15, 45),
(4, 18, 00);

INSERT INTO Data (ID_daty, Dzien, Miesiac, Rok, Dzien_tygodnia, Dzien_roboczy, Wakacje, Nazwa_miesiaca) VALUES
(1, 15, 5, 2023, 'Poniedziałek', 'Tak', 'Nie', 'Maj'),
(2, 20, 12, 2022, 'Wtorek', 'Tak', 'Nie', 'Grudzień'),
(3, 1, 11, 2024, 'Środa', 'Nie', 'Tak', 'Listopad'),
(4, 10, 10, 2024, 'Czwartek', 'Tak', 'Tak', 'Październik');

INSERT INTO Junk (ID_junk, Typ_trasy, Typ_sredniego_spalania) VALUES
(1, 'Krótka', 'Niskie'),
(2, 'Krótka', 'Wysokie'),
(3, 'Długa', 'Średnie'),
(4, 'Bardzo długa', 'Bardzo duże');

INSERT INTO Pojazd (ID_pojazdu, Typ, Elektryczny, Typ_pojemnosci_akumulatora, Czy_nadal_uzywany, Nazwa) VALUES
(1, 'Rower', 'Tak', 'Duża', 'Tak', 'Rower1'),
(2, 'Hulajnoga', 'Nie', 'Mała', 'Tak', 'Hulajnoga2'),
(3, 'Rower', 'Nie', 'Brak', 'Tak', 'Rower3'),
(4, 'Hulajnoga', 'Nie', 'Średnia', 'Nie', 'Hulajnoga4');

INSERT INTO Wypozyczenie_Junk (ID_junk, Poprawne_Odstawienie) VALUES
(1, 'Tak'),
(2, 'Nie');

INSERT INTO Wypozyczenie (ID_pojazdu, ID_uzytkownika, ID_stacja_startowa, ID_stacja_koncowa, ID_junk, ID_daty_startu, ID_czasu_startu, Koszt, Czas_wypozyczenia, Przejechany_dystans) VALUES
(1, 1, 1, 2, 1, 1, 1, 50.00, 120, 25.5),
(2, 2, 2, 3, 2, 2, 2, 20.00, 60, 15.0),
(3, 3, 3, 4, 2, 3, 3, 15.00, 45, 10.0),
(4, 4, 4, 1, 1, 4, 4, 70.00, 180, 35.0);

INSERT INTO Wykonanie_Wymiany_Akumulatora (ID_daty_trasy, Nr_trasy, ID_czasu_zakonczenia_trasy, ID_pojazdu, ID_junk) VALUES
(1, 101, 2, 1, 1),
(2, 102, 3, 2, 2),
(3, 103, 4, 3, 3),
(4, 104, 1, 4, 4);
