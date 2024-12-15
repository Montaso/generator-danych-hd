use PrzejazdDW

INSERT INTO [dbo].[Wypozyczenie_Junk] 
SELECT po, pdtss 
FROM 
	  (
		VALUES 
			  ('tak', 'tak')
			, ('nie', 'nie')
			, ('tak', 'nie')
			, ('nie', 'tak')
	  ) AS Kombinacje(po, pdtss);

SELECT * FROM PrzejazdDW.dbo.Wypozyczenie_Junk;
