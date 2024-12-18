use Przejazd

SET DATEFORMAT DMY;

BULK INSERT Uzytkownicy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/users.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Pojazdy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/vehicles_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Vany
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/vans_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a'
);

BULK INSERT Kierowcy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/drivers.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Stacje
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/stations_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wypozyczenia
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/rentals_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Trasy_Vanow
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/van_routes_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

BULK INSERT Wymiany_Akumulatorow
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data/battery_replacements_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

