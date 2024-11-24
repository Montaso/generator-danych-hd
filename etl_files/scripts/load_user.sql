use PrzejazdDW

If (object_id('vETLDimUzytkownicy') is not null) Drop View vETLDimUzytkownicy;
go
CREATE VIEW vETLDimUzytkownicy
AS
SELECT
	Imie + ' ' + Nazwisko AS Imie_i_nazwisko,
	PESEL
FROM Przejazd.dbo.Uzytkownicy;
go

MERGE INTO Uzytkownik as TT
	USING vETLDimUzytkownicy as ST
		ON TT.Imie_i_nazwisko = ST.Imie_i_nazwisko
			WHEN NOT MATCHED THEN
				INSERT (Imie_i_nazwisko, PESEL)
				VALUES (ST.Imie_i_nazwisko, ST.PESEL)
			WHEN NOT MATCHED BY SOURCE THEN
				DELETE;

drop view vETLDimUzytkownicy;

use PrzejazdDW
select * from Uzytkownik