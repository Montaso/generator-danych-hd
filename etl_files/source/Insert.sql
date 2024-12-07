USE Przejazd;

SET DATEFORMAT DMY;

DECLARE @folderPath NVARCHAR(MAX) = 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data';

DECLARE @sql NVARCHAR(MAX);
SET @sql = '
BULK INSERT Uzytkownicy
FROM ''' + @folderPath + '\users.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Pojazdy
FROM ''' + @folderPath + '\vehicles_data.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Vany
FROM ''' + @folderPath + '\vans_data.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''0x0a''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Kierowcy
FROM ''' + @folderPath + '\drivers.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Stacje
FROM ''' + @folderPath + '\stations_data.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Wypozyczenia
FROM ''' + @folderPath + '\rentals_data.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Trasy_Vanow
FROM ''' + @folderPath + '\van_routes_data.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SET @sql = '
BULK INSERT Wymiany_Akumulatorow
FROM ''' + @folderPath + '\battery_replacements_data.csv''
WITH (
    FORMAT = ''CSV'',
    FIRSTROW = 2,
    FIELDTERMINATOR = '';'',
    ROWTERMINATOR = ''\n''
);
';
EXEC sp_executesql @sql;

SELECT * FROM Wypozyczenia;
