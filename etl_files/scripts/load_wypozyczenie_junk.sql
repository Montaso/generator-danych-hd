use PrzejazdDW

INSERT INTO [dbo].[Wypozyczenie_Junk] 
SELECT po 
FROM 
	  (
		VALUES 
			  ('tak')
			, ('nie')
	  ) 
	AS Poprawne_odstawienie(po);

select * from PrzejazdDW.dbo.Wypozyczenie_Junk