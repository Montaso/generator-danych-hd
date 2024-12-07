use PrzejazdDW

INSERT INTO [dbo].[Junk] 
SELECT tt, tss 
FROM 
	  (
		VALUES 
			  ('short')
			, ('medium')
			, ('long')
			, ('very long')
	  ) 
	AS Typ_trasy(tt)
	, (
		VALUES 
			  ('small')
			, ('medium')
			, ('big')
			, ('very big')
	  ) 
	AS Typ_sredniego_spalania(tss);

select * from PrzejazdDW.dbo.Junk