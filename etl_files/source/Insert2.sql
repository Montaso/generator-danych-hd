use Przejazd

SET DATEFORMAT DMY;

BULK INSERT Uzytkownicy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data\users12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Pojazdy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/vehicles_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n'
);

BULK INSERT Vany
FROM '/data/vans_data2.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a'
);

BULK INSERT Kierowcy
FROM '/data/drivers2.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Stacje
FROM '/data/stations_data2.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wypozyczenia
FROM '/data/rentals_data2.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Trasy_Vanow
FROM '/data/van_routes_data2.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wymiany_Akumulatorow
FROM '/data/battery_replacements_data2.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

SELECT * FROM Kierowcy
SELECT * FROM Wymiany_Akumulatorow

