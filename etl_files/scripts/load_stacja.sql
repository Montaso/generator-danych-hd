USE PrzejazdDW;

IF (OBJECT_ID('vETLDimStacje') IS NOT NULL) 
    DROP VIEW vETLDimStacje;
GO

CREATE VIEW vETLDimStacje AS
SELECT
	CASE 
		WHEN Dlugosc_geograficzna BETWEEN 49.0 AND 49.4 THEN 'Wies'
		WHEN Dlugosc_geograficzna  BETWEEN 49.4 AND 50.0 THEN 'Obrzeza'
		WHEN Dlugosc_geograficzna  BETWEEN 50.0 AND 52.0 THEN 'Przedmiescia'
		WHEN Dlugosc_geograficzna  BETWEEN 52.0 AND 54.8 THEN 'Centrum miasta'
	END AS Lokalizacja,
	CASE
		WHEN Liczba_miejsc BETWEEN 5 AND 9 THEN 'small'
		WHEN Liczba_miejsc BETWEEN 10 AND 17 THEN 'medium'
		WHEN Liczba_miejsc BETWEEN 18 AND 24 THEN 'big'
		WHEN Liczba_miejsc > 24 THEN 'huge'
	END AS Wielkosc,
	CASE 
        WHEN Czy_aktualna = 1 THEN 'tak'
        WHEN Czy_Aktualna = 0 THEN 'nie'
        ELSE 'Unknown'
    END AS Czy_aktualna,
    Nazwa
FROM Przejazd.dbo.Stacje;
GO

MERGE INTO Stacja AS TT
USING vETLDimStacje AS ST
ON TT.Nazwa = ST.Nazwa
WHEN MATCHED AND TT.Czy_aktualna <> ST.Czy_aktualna THEN
    UPDATE SET 
        TT.Czy_aktualna = ST.Czy_aktualna
WHEN NOT MATCHED THEN
    INSERT (Lokalizacja, Wielkosc, Czy_aktualna, Nazwa)
    VALUES (ST.Lokalizacja, ST.Wielkosc, ST.Czy_aktualna, ST.Nazwa)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;

DROP VIEW vETLDimStacje;
GO 

USE PrzejazdDW
SELECT * FROM Stacja


