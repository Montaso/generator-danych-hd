SET DATEFORMAT DMY;

BULK INSERT Uzytkownicy
FROM '/data/users12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Pojazdy
FROM '/data/vehicles_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Vany
FROM '/data/vans_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a'
);

BULK INSERT Kierowcy
FROM '/data/drivers12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Stacje
FROM '/data/stations_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wypozyczenia
FROM '/data/rentals_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Trasy_Vanow
FROM '/data/van_routes_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wymiany_Akumulatorow
FROM '/data/battery_replacements_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

SELECT * FROM Kierowcy
SELECT * FROM Wymiany_Akumulatorow

