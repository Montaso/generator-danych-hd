USE PrzejazdDW;

IF OBJECT_ID('vETLDimWypozyczenia') IS NOT NULL 
    DROP VIEW vETLDimWypozyczenia;
GO

CREATE VIEW vETLDimWypozyczenia AS
SELECT
    ST.FK_ID_pojazdu AS ID_pojazdu,
    ST.FK_ID_uzytkownika AS ID_uzytkownika,
    ST.FK_Stacja_startowa AS ID_stacja_startowa,
    ST.FK_Stacja_koncowa AS ID_stacja_koncowa,
    Junk.ID_junk,
    DataDim.ID_daty AS ID_daty_startu,
    TimeDim.ID_czasu AS ID_czasu_startu,
    ST.Koszt,
    ST.Czas_wypozyczenia,
    ST.Przejechany_dystans
FROM
    Przejazd.dbo.Wypozyczenia AS ST
    JOIN Data AS DataDim 
        ON DataDim.Dzien = DAY(ST.Data_startu)
        AND DataDim.Miesiac = MONTH(ST.Data_startu)
        AND DataDim.Rok = YEAR(ST.Data_startu)
    JOIN Czas AS TimeDim 
        ON TimeDim.Godzina = DATEPART(HOUR, ST.Czas_startu)
        AND TimeDim.Minuta = DATEPART(MINUTE, ST.Czas_startu)
    JOIN Wypozyczenie_Junk AS Junk 
        ON Junk.Poprawne_odstawienie = 
            CASE 
                WHEN ST.Poprawne_odstawienie = 1 THEN 'tak'
                WHEN ST.Poprawne_odstawienie = 0 THEN 'nie'
            END
		AND Junk.Powrot_do_tej_samej_stacji = 
			CASE
				WHEN ST.FK_Stacja_startowa = ST.FK_Stacja_koncowa THEN 'tak'
				WHEN ST.FK_Stacja_startowa != ST.FK_Stacja_koncowa THEN 'nie'
			END
GO

MERGE INTO Wypozyczenie AS TT
USING vETLDimWypozyczenia AS ST
ON 
    TT.ID_pojazdu = ST.ID_pojazdu
    AND TT.ID_uzytkownika = ST.ID_uzytkownika
    AND TT.ID_daty_startu = ST.ID_daty_startu
    AND TT.ID_czasu_startu = ST.ID_czasu_startu
WHEN NOT MATCHED THEN
    INSERT (
        ID_pojazdu,
        ID_uzytkownika,
        ID_stacja_startowa,
        ID_stacja_koncowa,
        ID_junk,
        ID_daty_startu,
        ID_czasu_startu,
        Koszt,
        Czas_wypozyczenia,
        Przejechany_dystans
    )
    VALUES (
        ST.ID_pojazdu,
        ST.ID_uzytkownika,
        ST.ID_stacja_startowa,
        ST.ID_stacja_koncowa,
        ST.ID_junk,
        ST.ID_daty_startu,
        ST.ID_czasu_startu,
        ST.Koszt,
        ST.Czas_wypozyczenia,
        ST.Przejechany_dystans
    );
GO

DROP VIEW vETLDimWypozyczenia;
GO

SELECT * FROM PrzejazdDW.dbo.Wypozyczenie;
