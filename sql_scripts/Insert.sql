SET DATEFORMAT DMY;

BULK INSERT Uzytkownicy
FROM '/data/users.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
);

SELECT * FROM Uzytkownicy;