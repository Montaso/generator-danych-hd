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
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Vany
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/vans_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a'
);

BULK INSERT Kierowcy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/drivers12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Stacje
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/stations_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wypozyczenia
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/rentals_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Trasy_Vanow
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/van_routes_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wymiany_Akumulatorow
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/battery_replacements_data12.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

