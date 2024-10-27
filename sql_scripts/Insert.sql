SET DATEFORMAT DMY;

BULK INSERT Uzytkownicy
FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data\users.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    CODEPAGE = '65001'
);

SELECT * FROM Uzytkownicy;
