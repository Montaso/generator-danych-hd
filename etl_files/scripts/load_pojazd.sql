USE PrzejazdDW;

IF (OBJECT_ID('vETLDimPojazdy') IS NOT NULL) 
    DROP VIEW vETLDimPojazdy;
GO

CREATE VIEW vETLDimPojazdy AS
SELECT
    ID_pojazdu,
    Typ,
    CASE 
        WHEN Elektryczny = 1 THEN 'Yes'
        WHEN Elektryczny = 0 THEN 'No'
        ELSE 'Unknown'
    END AS Elektryczny,
    CASE
        WHEN Pojemnosc_akumulatora BETWEEN 500 AND 700 THEN 'Small'
        WHEN Pojemnosc_akumulatora BETWEEN 701 AND 900 THEN 'Medium'
        WHEN Pojemnosc_akumulatora BETWEEN 901 AND 1000 THEN 'Large'
        ELSE 'Unknown'
    END AS Typ_pojemnosci_akumulatora,
    CASE 
        WHEN Czy_nadal_uzywany = 1 THEN 'Yes'
        WHEN Czy_nadal_uzywany = 0 THEN 'No'
        ELSE 'Unknown'
    END AS Czy_nadal_uzywany,
    Nazwa
FROM Przejazd.dbo.Pojazdy;
GO

MERGE INTO Pojazd AS TT
USING vETLDimPojazdy AS ST
ON TT.ID_pojazdu = ST.ID_pojazdu
WHEN NOT MATCHED THEN
    INSERT (ID_pojazdu, Typ, Elektryczny, Typ_pojemnosci_akumulatora, Czy_nadal_uzywany, Nazwa)
    VALUES (ST.ID_pojazdu, ST.Typ, ST.Elektryczny, ST.Typ_pojemnosci_akumulatora, ST.Czy_nadal_uzywany, ST.Nazwa)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
GO

DROP VIEW vETLDimPojazdy;
GO

SELECT * FROM Pojazd
