SET DATEFORMAT DMY;
DECLARE @StartDate DATE = '01-01-1950';
DECLARE @EndDate DATE = '01-01-2024';

WITH DateRange AS (
    SELECT CAST(@StartDate AS DATE) AS DateValue
    UNION ALL
    SELECT DATEADD(DAY, 1, DateValue)
    FROM DateRange
    WHERE DateValue < @EndDate
)
INSERT INTO [dbo].[Data]
SELECT
    DAY(DateValue) AS Dzien,
    MONTH(DateValue) AS Miesiac,
    YEAR(DateValue) AS Rok,
    DATENAME(WEEKDAY, DateValue) AS Dzien_tygodnia,
    CASE WHEN DATENAME(WEEKDAY, DateValue) IN ('Saturday', 'Sunday') THEN 'nie' ELSE 'tak' END AS Dzien_roboczy,
    CASE 
        WHEN MONTH(DateValue) IN (7, 8) THEN 'tak'
        ELSE 'nie'
    END AS Wakacje,
    DATENAME(MONTH, DateValue) AS Nazwa_miesiaca
FROM DateRange
OPTION (MAXRECURSION 0);

use PrzejazdDW
select * from Data
