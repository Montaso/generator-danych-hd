USE PrzejazdDW;
SET DATEFORMAT DMY;

IF OBJECT_ID('vETL_Wykonanie_Wymiany_Akumulatora') IS NOT NULL
    DROP VIEW vETL_Wykonanie_Wymiany_Akumulatora;
GO

If (object_id('dbo.RaportsTemp') is not null) DROP TABLE dbo.RaportsTemp;
CREATE TABLE dbo.RaportsTemp(
	route_id INT NOT NULL, 
	route_length DECIMAL NOT NULL, 
	route_time TIME NOT NULL, 
	average_fuel_consumption DECIMAL NOT NULL, 
	route_date DATE NOT NULL,
	finish_time TIME NOT NULL,
	moved_bikes SMALLINT NOT NULL,
	moved_scooters SMALLINT NOT NULL
);
go

BULK INSERT dbo.RaportsTemp
    FROM 'C:\Users\Adrian\Desktop\Studia\sem 5\HD\generator-danych-hd\generated_data\reports12.csv'
    WITH
    (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n'
    )
go

CREATE VIEW vETL_Wykonanie_Wymiany_Akumulatora AS
SELECT 
    DataDim.ID_daty AS ID_daty_trasy,
    TV.ID_trasy AS Nr_trasy,
    TimeDim.ID_czasu AS ID_czasu_zakonczenia_trasy,
    pojazdy.ID_pojazdu AS ID_pojazdu,
	junk.ID_junk AS ID_junk
FROM 
    Przejazd.dbo.Trasy_Vanow AS TV
	JOIN dbo.RaportsTemp AS raport
		ON raport.route_id = TV.ID_trasy
	JOIN Data AS DataDim
		ON DataDim.Dzien = DAY(TV.Data_trasy)
        AND DataDim.Miesiac = MONTH(TV.Data_trasy)
        AND DataDim.Rok = YEAR(TV.Data_trasy)
	JOIN Czas AS TimeDim
        ON TimeDim.Godzina = DATEPART(HOUR, raport.finish_time)
        AND TimeDim.Minuta = DATEPART(MINUTE, raport.finish_time)
	JOIN Przejazd.dbo.Wymiany_Akumulatorow AS wymiany
		ON wymiany.FK_ID_trasy = TV.ID_trasy
	JOIN Przejazd.dbo.Pojazdy AS pojazdy
		ON pojazdy.ID_pojazdu = wymiany.FK_ID_pojazdu
	JOIN PrzejazdDW.dbo.Junk AS junk
		ON junk.Typ_trasy = 
        CASE
            WHEN raport.route_length <= 60 THEN 'short'
            WHEN raport.route_length <= 90 THEN 'medium'
            WHEN raport.route_length <= 120 THEN 'long'
            ELSE 'very long'
        END
    AND junk.Typ_sredniego_spalania = 
        CASE
            WHEN raport.average_fuel_consumption <= 11 THEN 'small'
            WHEN raport.average_fuel_consumption <= 12 THEN 'medium'
            WHEN raport.average_fuel_consumption <= 13 THEN 'big'
            ELSE 'very big'
        END;	
GO

USE PrzejazdDW;

MERGE INTO PrzejazdDW.dbo.Wykonanie_Wymiany_Akumulatora AS TT
USING vETL_Wykonanie_Wymiany_Akumulatora AS ST
ON 
    TT.ID_daty_trasy = ST.ID_daty_trasy
    AND TT.Nr_trasy = ST.Nr_trasy
    AND TT.ID_czasu_zakonczenia_trasy = ST.ID_czasu_zakonczenia_trasy
    AND TT.ID_pojazdu = ST.ID_pojazdu
    AND TT.ID_junk = ST.ID_junk
WHEN NOT MATCHED THEN
    INSERT (
        ID_daty_trasy,
        Nr_trasy,
        ID_czasu_zakonczenia_trasy,
        ID_pojazdu,
        ID_junk
    )
    VALUES (
        ST.ID_daty_trasy,
        ST.Nr_trasy,
        ST.ID_czasu_zakonczenia_trasy,
        ST.ID_pojazdu,
        ST.ID_junk
    );

GO

drop view vETL_Wykonanie_Wymiany_Akumulatora
drop table dbo.RaportsTemp

select * from Wykonanie_Wymiany_Akumulatora